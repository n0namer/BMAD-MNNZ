"""Pytest configuration and shared fixtures."""

import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))


def pytest_configure(config):  # type: ignore
    """Configure pytest."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "asyncio: mark test as async")
    config.addinivalue_line("markers", "ux001: mark test for UX-001 story")
    config.addinivalue_line("markers", "acceptance: mark test as acceptance test")
    config.addinivalue_line("markers", "callbacks: mark test as callback test")
    config.addinivalue_line("markers", "kelly: mark test as Kelly criterion test")

    # Configure asyncio mode
    if not hasattr(config.option, 'asyncio_mode'):
        config.option.asyncio_mode = 'auto'
