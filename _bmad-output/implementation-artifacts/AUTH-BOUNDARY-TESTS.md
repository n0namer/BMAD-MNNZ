---
phase: "phase2"
category: "auth-boundary-coverage"
status: "GENERATED"
generatedDate: "2026-02-26T18:30:00Z"
totalTests: 2
coverageIncrease: "90% → 100%"
---

# Auth Boundary Tests Specification

**Phase 2 Gap Closure: Auth/AuthZ Boundary Validation (2 Tests)**

---

## Executive Summary

Auth boundary tests validate cross-role access control violations and permission escalation attempts. These 2 tests close critical security gaps in Phase 1 (90% → 100% auth coverage).

**Impact**: Raises auth/authz boundary coverage from 90% → 100%

---

## Test 1: Cross-Role Boundary - Resource Access Violation

**Epic**: E-AUDIT-TRAIL
**Security Category**: Authorization (Role-Based Access Control)
**Priority**: P1 (Security)
**Risk Score**: 9/10 (Critical)
**Effort**: 1 hour

### Test Name
`AUTH_BOUNDARY_CROSS_ROLE_RESOURCE_VIOLATION`

### Description
Validates that users with one role cannot access resources assigned to another role. Tests the boundary where a VIEWER role attempts to access OPERATOR-only resources.

### Test Scenario
```
Roles and Permissions:
- ADMIN: Full access to all strategies and audit logs
- OPERATOR: Can approve strategies, view own audit logs
- VIEWER: Can only view public summaries, NO audit access

Resource: audit_log_id = "audit-12345"
- Owner: strategy_operator_user
- Visibility: OPERATOR_ONLY

Attack Scenario:
- viewer_user attempts to retrieve audit_log_id
- endpoint: GET /api/v1/audit_logs/audit-12345
```

### Test Steps
```gherkin
Given two users with different roles:
  - operator_user has role OPERATOR
  - viewer_user has role VIEWER
  And an audit log exists:
    - audit_log_id: "audit-12345"
    - owner: operator_user
    - visibility: OPERATOR_ONLY
    - content: full execution trace (sensitive)

# Test Case 1: VIEWER accessing OPERATOR resource
When viewer_user requests:
  - GET /api/v1/audit_logs/audit-12345
  - Authorization header: viewer_user's auth token
Then the system SHOULD:
  - Return 403 Forbidden (NOT 404, to avoid info leak)
  - Include error: "Insufficient permissions to access this resource"
  - Audit log entry created with:
    - event_type: UNAUTHORIZED_ACCESS_ATTEMPT
    - user_id: viewer_user
    - resource_id: audit-12345
    - timestamp: current UTC
  - Audit log NOT returned to viewer_user
  - Returned audit log NOT include sensitive details

# Test Case 2: VIEWER listing audit logs (should see none)
When viewer_user requests:
  - GET /api/v1/audit_logs?strategy_id=strategy-1
  - Authorization header: viewer_user's auth token
Then the system SHOULD:
  - Return 200 OK (not error)
  - Result: empty list [] (not 403, different from accessing specific resource)
  - Audit log entries created for attempt
  - Sensitive logs not included

# Test Case 3: OPERATOR accessing own audit logs (should succeed)
When operator_user requests:
  - GET /api/v1/audit_logs/audit-12345
  - Authorization header: operator_user's auth token
Then the system SHOULD:
  - Return 200 OK
  - Response includes full audit log (sensitive details)
  - No unauthorized_access audit entry

# Test Case 4: Cross-organization boundary (if multi-tenant)
When viewer_user_org_A requests:
  - GET /api/v1/audit_logs/audit-12345 (from org_B)
  - Authorization header: org_A viewer token
Then the system SHOULD:
  - Return 403 Forbidden
  - Include error: "Cross-organization access denied"
  - Audit log for denied access recorded
```

### Acceptance Criteria
- ✅ Viewer cannot access operator audit logs (403 Forbidden)
- ✅ Unauthorized access attempt logged with details
- ✅ Error response doesn't leak resource existence (403 not 404)
- ✅ Operator can access own audit logs (200 OK)
- ✅ Sensitive content protected from lower-privilege users
- ✅ All access attempts audited (successful AND denied)

### Test Code Template
```python
def test_auth_boundary_cross_role_resource_violation():
    """AUTH_BOUNDARY_CROSS_ROLE_RESOURCE_VIOLATION"""
    api = AuditAPI()

    # Setup users
    operator = create_user(role="OPERATOR")
    viewer = create_user(role="VIEWER")

    # Setup audit log (created by operator)
    audit_log = api.create_audit_log(
        user=operator,
        strategy_id="strategy-1",
        event="APPROVAL",
        visibility="OPERATOR_ONLY"
    )

    # Case 1: Viewer accessing operator's audit log
    with viewer.auth_context():
        response = api.get(f"/audit_logs/{audit_log.id}")

    assert response.status_code == 403, "Should deny viewer access"
    error = response.json()
    assert "permission" in error["error"].lower()

    # Verify attempt was logged
    access_attempts = api.query_audit_log(
        event_type="UNAUTHORIZED_ACCESS_ATTEMPT",
        user_id=viewer.id
    )
    assert len(access_attempts) > 0, "Unauthorized attempt should be logged"

    # Case 2: Viewer listing audit logs (should be empty)
    with viewer.auth_context():
        response = api.get("/audit_logs?strategy_id=strategy-1")

    assert response.status_code == 200, "List should succeed"
    assert response.json()["items"] == [], "Should return empty list"

    # Case 3: Operator accessing own audit log (should succeed)
    with operator.auth_context():
        response = api.get(f"/audit_logs/{audit_log.id}")

    assert response.status_code == 200, "Operator should access own log"
    assert response.json()["id"] == audit_log.id

    # Case 4: Sensitive content not in unauthorized response
    assert "sensitive_content" not in response.json() or \
           response.status_code != 403
```

---

## Test 2: Permission Escalation - Operator Attempting Admin Action

**Epic**: E-STRATEGY-LIFECYCLE
**Security Category**: Authorization (Privilege Escalation Prevention)
**Priority**: P1 (Security)
**Risk Score**: 9/10 (Critical)
**Effort**: 1 hour

### Test Name
`AUTH_BOUNDARY_PERMISSION_ESCALATION_ATTEMPT`

### Description
Validates that users cannot escalate privileges by attempting admin-only actions. Tests an OPERATOR attempting to modify system configuration (admin-only).

### Test Scenario
```
Roles and Permissions:
- ADMIN: Can modify system config, user roles, create new operators
- OPERATOR: Can approve strategies, manage own approvals
- VIEWER: Read-only access

Admin Action: Update user role
- endpoint: PATCH /api/v1/users/{user_id}/role
- Requires: admin:user:manage scope

Attack Scenario:
- operator_user attempts to make another user an admin
- endpoint: PATCH /api/v1/users/viewer_user/role
- payload: {"role": "ADMIN"}
```

### Test Steps
```gherkin
Given users with different roles:
  - admin_user has role ADMIN
  - operator_user has role OPERATOR
  - viewer_user has role VIEWER

# Test Case 1: OPERATOR attempting to escalate another user
When operator_user requests:
  - PATCH /api/v1/users/viewer_user/role
  - body: {"role": "ADMIN"}
  - Authorization header: operator_user's auth token
Then the system SHOULD:
  - Return 403 Forbidden
  - Include error: "Insufficient permissions for admin:user:manage"
  - user role NOT changed (still VIEWER)
  - Privilege escalation attempt logged:
    - event_type: ESCALATION_ATTEMPT
    - from_role: OPERATOR
    - target_action: admin:user:manage
    - timestamp: current UTC
  - Alert generated to admin

# Test Case 2: OPERATOR attempting to self-escalate
When operator_user requests:
  - PATCH /api/v1/users/operator_user/role
  - body: {"role": "ADMIN"}
  - Authorization header: operator_user's auth token
Then the system SHOULD:
  - Return 403 Forbidden
  - Include error: "Cannot modify own role (requires admin approval)"
  - Self-escalation attempt logged
  - Stricter alert (self-escalation is higher risk)

# Test Case 3: OPERATOR attempting system config modification
When operator_user requests:
  - PATCH /api/v1/system/config
  - body: {"timeout_seconds": 1} (reduce timeout)
  - Authorization header: operator_user's auth token
Then the system SHOULD:
  - Return 403 Forbidden
  - Include error: "Insufficient permissions for admin:system:configure"
  - Config NOT modified
  - Unauthorized modification attempt logged

# Test Case 4: ADMIN performing same action (should succeed)
When admin_user requests:
  - PATCH /api/v1/users/viewer_user/role
  - body: {"role": "OPERATOR"}
  - Authorization header: admin_user's auth token
Then the system SHOULD:
  - Return 200 OK
  - user role changed to OPERATOR
  - role change logged with actor: admin_user
```

### Acceptance Criteria
- ✅ Operator cannot escalate other users (403 Forbidden)
- ✅ Operator cannot self-escalate (403 Forbidden)
- ✅ Escalation attempts logged as ESCALATION_ATTEMPT
- ✅ Admin can perform privileged actions (200 OK)
- ✅ Clear error messages (don't indicate whether action exists)
- ✅ Alerts generated for escalation attempts
- ✅ No privilege escalation possible through API

### Test Code Template
```python
def test_auth_boundary_permission_escalation_attempt():
    """AUTH_BOUNDARY_PERMISSION_ESCALATION_ATTEMPT"""
    api = UserAPI()

    # Setup users
    admin = create_user(role="ADMIN")
    operator = create_user(role="OPERATOR")
    viewer = create_user(role="VIEWER")

    # Case 1: Operator attempting to escalate viewer
    with operator.auth_context():
        response = api.patch(
            f"/users/{viewer.id}/role",
            json={"role": "ADMIN"}
        )

    assert response.status_code == 403, "Should deny escalation"
    assert "permission" in response.json()["error"].lower()

    # Verify role unchanged
    viewer_updated = api.get(f"/users/{viewer.id}")
    assert viewer_updated.json()["role"] == "VIEWER"

    # Verify attempt logged
    escalation_attempts = api.query_audit_log(
        event_type="ESCALATION_ATTEMPT",
        user_id=operator.id
    )
    assert len(escalation_attempts) > 0

    # Case 2: Operator self-escalate
    with operator.auth_context():
        response = api.patch(
            f"/users/{operator.id}/role",
            json={"role": "ADMIN"}
        )

    assert response.status_code == 403

    # Case 3: System config modification
    with operator.auth_context():
        response = api.patch(
            "/system/config",
            json={"timeout_seconds": 1}
        )

    assert response.status_code == 403

    # Case 4: Admin performing same action
    with admin.auth_context():
        response = api.patch(
            f"/users/{viewer.id}/role",
            json={"role": "OPERATOR"}
        )

    assert response.status_code == 200
    viewer_updated = api.get(f"/users/{viewer.id}")
    assert viewer_updated.json()["role"] == "OPERATOR"

    # Verify success logged
    success_logs = api.query_audit_log(
        event_type="ROLE_CHANGED",
        actor_id=admin.id
    )
    assert len(success_logs) > 0
```

---

## Security Impact

### Attack Vectors Addressed
| Attack Vector | Test | Mitigation |
|---------------|------|-----------|
| Direct resource access | Cross-role boundary | 403 Forbidden + no info leak |
| Privilege escalation | Permission escalation | 403 + audit + alert |
| Audit log tampering | Both tests | All access attempts logged |
| Role confusion | Both tests | Clear role enforcement |
| Lateral movement | Cross-role boundary | Strict RBAC boundaries |

### Audit Trail Requirements

Both tests require comprehensive audit logging:

```
UNAUTHORIZED_ACCESS_ATTEMPT event:
{
  "event_type": "UNAUTHORIZED_ACCESS_ATTEMPT",
  "timestamp": "2026-02-27T10:30:45.123Z",
  "user_id": "{user_id}",
  "user_role": "VIEWER",
  "resource_id": "{resource_id}",
  "resource_type": "audit_log",
  "action_attempted": "read",
  "reason_denied": "insufficient_permissions",
  "source_ip": "192.168.1.100",
  "user_agent": "Mozilla/5.0..."
}

ESCALATION_ATTEMPT event:
{
  "event_type": "ESCALATION_ATTEMPT",
  "timestamp": "2026-02-27T10:31:00.456Z",
  "user_id": "{user_id}",
  "user_role": "OPERATOR",
  "target_user_id": "{viewer_user_id}",
  "action_attempted": "modify_role_to_admin",
  "result": "denied",
  "scope_required": "admin:user:manage",
  "severity": "HIGH"
}
```

---

## Coverage Summary

| Test | Epic | Scenario | Severity | Status |
|------|------|----------|----------|--------|
| AUTH_BOUNDARY_CROSS_ROLE_RESOURCE_VIOLATION | E-AUDIT-TRAIL | VIEWER accessing OPERATOR resource | CRITICAL | ✅ Designed |
| AUTH_BOUNDARY_PERMISSION_ESCALATION_ATTEMPT | E-STRATEGY-LIFECYCLE | OPERATOR escalating privileges | CRITICAL | ✅ Designed |

**Total Auth Boundary Tests**: 2
**Coverage Increase**: 90% → 100%
**Estimated Effort**: 2 hours
**Security Impact**: Prevents critical authorization bypasses
**Status**: Ready for Phase 2 Week 2 implementation

---

**Generated**: 2026-02-26 18:30:00Z
**Part of**: Phase 2 Gap Closure (10-12 tests total)
**Next**: Template Expansion Tests (53 tests for BLOCKER-3/4/5)
