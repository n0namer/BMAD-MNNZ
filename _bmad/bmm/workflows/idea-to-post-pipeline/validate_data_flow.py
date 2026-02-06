#!/usr/bin/env python3
"""
Content Machine Pipeline - Data Flow Validation Script
QA-Ready: Run after each test phase to validate data consistency

Usage:
    python3 validate_data_flow.py --mode text --data-dir D:\test-content-machine\data
    python3 validate_data_flow.py --mode routine --data-dir D:\test-content-machine\data
    python3 validate_data_flow.py --mode both --data-dir D:\test-content-machine\data
"""

import csv
import json
import sys
import argparse
from pathlib import Path
from typing import Tuple, List, Dict


class DataFlowValidator:
    """Validate Content Machine Pipeline data flows"""

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.ideas_file = self.data_dir / "ideas_inbox.csv"
        self.research_file = self.data_dir / "ideas_research.csv"
        self.posts_file = self.data_dir / "posts_content.csv"

        self.ideas = []
        self.research = []
        self.posts = []
        self.errors = []
        self.warnings = []

    def load_csvs(self) -> bool:
        """Load CSV files"""
        try:
            with open(self.ideas_file, 'r', encoding='utf-8') as f:
                self.ideas = list(csv.DictReader(f))
            with open(self.research_file, 'r', encoding='utf-8') as f:
                self.research = list(csv.DictReader(f))
            with open(self.posts_file, 'r', encoding='utf-8') as f:
                self.posts = list(csv.DictReader(f))
            return True
        except FileNotFoundError as e:
            self.errors.append(f"File not found: {e}")
            return False

    def validate_text_mode(self) -> bool:
        """Validate TEXT mode data flow"""
        print("\n" + "="*60)
        print("VALIDATING TEXT MODE DATA FLOW")
        print("="*60)

        success = True

        # Filter TEXT mode ideas
        text_ideas = [i for i in self.ideas if i.get('content_type', '') != 'demo']

        if not text_ideas:
            self.warnings.append("No TEXT mode ideas found")
            return True

        for idea in text_ideas:
            idea_id = idea.get('id')
            print(f"\nValidating idea {idea_id}...")

            # Check source
            if idea.get('source') != 'user_input':
                self.errors.append(f"Idea {idea_id}: source should be 'user_input', got '{idea.get('source')}'")
                success = False

            # Check no idea_metadata
            if 'idea_metadata' in idea and idea.get('idea_metadata'):
                self.errors.append(f"Idea {idea_id}: TEXT mode should NOT have idea_metadata")
                success = False

            # Find research for this idea
            research_rows = [r for r in self.research if r.get('original_idea_id') == idea_id]

            if not research_rows:
                self.errors.append(f"Idea {idea_id}: No research found")
                success = False
                continue

            research = research_rows[0]

            # Check NO pain_points_json
            if 'pain_points_json' in research:
                if research.get('pain_points_json'):
                    self.errors.append(f"Idea {idea_id}: TEXT mode has pain_points_json (shouldn't!)")
                    success = False

            # Count variants
            variants = [p for p in self.posts if p.get('idea_id') == idea_id]

            if len(variants) != 3:
                self.errors.append(f"Idea {idea_id}: Expected 3 variants, got {len(variants)}")
                success = False
            else:
                print(f"  ✓ Correct variant count: 3")

            # Check variant types
            for variant in variants:
                if variant.get('variant_type') != 'base':
                    self.errors.append(
                        f"Idea {idea_id}: Variant {variant.get('id')} "
                        f"has type '{variant.get('variant_type')}', expected 'base'"
                    )
                    success = False

                # Check no pain/offer embedding
                if variant.get('pain_embedded') == 'true':
                    self.errors.append(
                        f"Idea {idea_id}: TEXT variant {variant.get('id')} "
                        f"has pain_embedded=true (shouldn't!)"
                    )
                    success = False

                if variant.get('offer_embedded') == 'true':
                    self.errors.append(
                        f"Idea {idea_id}: TEXT variant {variant.get('id')} "
                        f"has offer_embedded=true (shouldn't!)"
                    )
                    success = False

        return success

    def validate_routine_mode(self) -> bool:
        """Validate ROUTINE mode data flow"""
        print("\n" + "="*60)
        print("VALIDATING ROUTINE MODE DATA FLOW")
        print("="*60)

        success = True

        # Filter ROUTINE mode ideas
        routine_ideas = [i for i in self.ideas if i.get('content_type') == 'demo']

        if not routine_ideas:
            self.warnings.append("No ROUTINE mode ideas found")
            return True

        for idea in routine_ideas:
            idea_id = idea.get('id')
            print(f"\nValidating idea {idea_id}...")

            # Check source
            if idea.get('source') != 'routine':
                self.errors.append(f"Idea {idea_id}: ROUTINE source should be 'routine', got '{idea.get('source')}'")
                success = False

            # Check idea_metadata exists and is valid JSON
            if not idea.get('idea_metadata'):
                self.errors.append(f"Idea {idea_id}: ROUTINE mode missing idea_metadata")
                success = False
            else:
                try:
                    metadata = json.loads(idea.get('idea_metadata'))
                    required_keys = ['visual_context', 'tools_used', 'demonstrated_result', 'context_type']
                    for key in required_keys:
                        if key not in metadata:
                            self.errors.append(f"Idea {idea_id}: metadata missing '{key}'")
                            success = False
                except json.JSONDecodeError:
                    self.errors.append(f"Idea {idea_id}: Invalid JSON in idea_metadata")
                    success = False

            # Find research for this idea
            research_rows = [r for r in self.research if r.get('original_idea_id') == idea_id]

            if not research_rows:
                self.errors.append(f"Idea {idea_id}: No research found")
                success = False
                continue

            research = research_rows[0]

            # Check pain_points_json exists and is valid
            if 'pain_points_json' not in research:
                self.errors.append(f"Idea {idea_id}: ROUTINE mode missing pain_points_json column")
                success = False
            elif not research.get('pain_points_json'):
                self.errors.append(f"Idea {idea_id}: pain_points_json is empty")
                success = False
            else:
                try:
                    pains = json.loads(research.get('pain_points_json'))

                    # Validate pain structure
                    for angle_name, angle_data in pains.items():
                        if 'pains' not in angle_data:
                            self.errors.append(
                                f"Idea {idea_id}: Angle '{angle_name}' missing 'pains' field"
                            )
                            success = False
                        else:
                            pain_count = len(angle_data['pains'])
                            if not 3 <= pain_count <= 5:
                                self.errors.append(
                                    f"Idea {idea_id}: Angle '{angle_name}' has {pain_count} pains, "
                                    f"expected 3-5"
                                )
                                success = False

                    print(f"  ✓ Pain points valid: {len(pains)} angles")

                except json.JSONDecodeError:
                    self.errors.append(f"Idea {idea_id}: Invalid JSON in pain_points_json")
                    success = False

            # Count variants - should be 6
            variants = [p for p in self.posts if p.get('idea_id') == idea_id]

            if len(variants) != 6:
                self.errors.append(f"Idea {idea_id}: Expected 6 variants, got {len(variants)}")
                success = False
            else:
                print(f"  ✓ Correct variant count: 6")

            # Check variant composition
            base_variants = [v for v in variants if v.get('variant_type') == 'base']
            cm_variants = [v for v in variants if v.get('variant_type', '').startswith('cm_')]

            if len(base_variants) < 1:
                self.errors.append(f"Idea {idea_id}: Expected >=1 base variant")
                success = False

            if len(cm_variants) < 3:
                self.errors.append(f"Idea {idea_id}: Expected >=3 CM variants, got {len(cm_variants)}")
                success = False

            # Check base variants
            for variant in base_variants:
                if variant.get('pain_embedded') != 'false':
                    self.errors.append(
                        f"Idea {idea_id}: Base variant {variant.get('id')} "
                        f"pain_embedded should be 'false'"
                    )
                    success = False

                if variant.get('offer_embedded') != 'false':
                    self.errors.append(
                        f"Idea {idea_id}: Base variant {variant.get('id')} "
                        f"offer_embedded should be 'false'"
                    )
                    success = False

            # Check CM variants
            for variant in cm_variants:
                if variant.get('pain_embedded') != 'true':
                    self.errors.append(
                        f"Idea {idea_id}: CM variant {variant.get('id')} "
                        f"pain_embedded should be 'true'"
                    )
                    success = False

                if variant.get('offer_embedded') != 'true':
                    self.errors.append(
                        f"Idea {idea_id}: CM variant {variant.get('id')} "
                        f"offer_embedded should be 'true'"
                    )
                    success = False

                framework = variant.get('variant_framework')
                valid_frameworks = ['PAS', 'Hook-Story-Offer', 'Show Your Work']
                if framework not in valid_frameworks:
                    self.errors.append(
                        f"Idea {idea_id}: Variant {variant.get('id')} "
                        f"has invalid framework '{framework}'"
                    )
                    success = False

        return success

    def validate_csv_schemas(self) -> bool:
        """Validate CSV column schemas"""
        print("\n" + "="*60)
        print("VALIDATING CSV SCHEMAS")
        print("="*60)

        success = True

        # Check ideas_inbox.csv
        print("\nChecking ideas_inbox.csv...")
        required_cols = ['id', 'date_added', 'source', 'raw_idea', 'content_type', 'category', 'status', 'notes']
        if self.ideas:
            for col in required_cols:
                if col not in self.ideas[0].keys():
                    self.errors.append(f"ideas_inbox.csv: Missing column '{col}'")
                    success = False
            if success:
                print("  ✓ All required columns present")

        # Check ideas_research.csv
        print("Checking ideas_research.csv...")
        required_cols = ['id', 'original_idea_id', 'research_date', 'main_angle', 'sub_angles_count',
                        'best_angle_id', 'angles_list', 'sources_count', 'avg_relevance']
        if self.research:
            for col in required_cols:
                if col not in self.research[0].keys():
                    self.errors.append(f"ideas_research.csv: Missing column '{col}'")
                    success = False
            if success:
                print("  ✓ All required columns present")

        # Check posts_content.csv
        print("Checking posts_content.csv...")
        required_cols = ['id', 'idea_id', 'research_id', 'angle_used', 'variant_type', 'draft_status',
                        'content_500_chars']
        if self.posts:
            for col in required_cols:
                if col not in self.posts[0].keys():
                    self.errors.append(f"posts_content.csv: Missing column '{col}'")
                    success = False
            if success:
                print("  ✓ All required columns present")

        return success

    def validate_numeric_fields(self) -> bool:
        """Validate numeric field types"""
        print("\n" + "="*60)
        print("VALIDATING NUMERIC FIELDS")
        print("="*60)

        success = True

        for i, row in enumerate(self.research):
            # Check sub_angles_count
            try:
                count = int(row.get('sub_angles_count', 0))
                if not 5 <= count <= 10:
                    self.warnings.append(
                        f"ideas_research row {i}: sub_angles_count={count} (typical 5-8)"
                    )
            except ValueError:
                self.errors.append(f"ideas_research row {i}: sub_angles_count not numeric")
                success = False

            # Check sources_count
            try:
                count = int(row.get('sources_count', 0))
                if count < 20:
                    self.warnings.append(
                        f"ideas_research row {i}: sources_count={count} (expect >=20)"
                    )
            except ValueError:
                self.errors.append(f"ideas_research row {i}: sources_count not numeric")
                success = False

            # Check avg_relevance
            try:
                relevance = int(row.get('avg_relevance', 0))
                if not 0 <= relevance <= 100:
                    self.errors.append(
                        f"ideas_research row {i}: avg_relevance={relevance} (must be 0-100)"
                    )
                    success = False
            except ValueError:
                self.errors.append(f"ideas_research row {i}: avg_relevance not numeric")
                success = False

        print("  ✓ Numeric field validation complete")
        return success

    def print_report(self):
        """Print validation report"""
        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)

        print(f"\nTotal errors: {len(self.errors)}")
        print(f"Total warnings: {len(self.warnings)}")

        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors:
            print("\n✅ ALL VALIDATIONS PASSED")

        return len(self.errors) == 0

    def run_all_validations(self) -> bool:
        """Run all validations"""
        if not self.load_csvs():
            print("❌ Failed to load CSV files")
            return False

        print("\nCSV Files Loaded:")
        print(f"  - ideas_inbox.csv: {len(self.ideas)} rows")
        print(f"  - ideas_research.csv: {len(self.research)} rows")
        print(f"  - posts_content.csv: {len(self.posts)} rows")

        success = True
        success &= self.validate_csv_schemas()
        success &= self.validate_numeric_fields()
        success &= self.validate_text_mode()
        success &= self.validate_routine_mode()

        self.print_report()

        return success


def main():
    parser = argparse.ArgumentParser(
        description="Validate Content Machine Pipeline data flows"
    )
    parser.add_argument(
        '--mode',
        choices=['text', 'routine', 'both'],
        default='both',
        help="Validation mode (text, routine, or both)"
    )
    parser.add_argument(
        '--data-dir',
        default='D:\\test-content-machine\\data',
        help="Path to data directory"
    )

    args = parser.parse_args()

    validator = DataFlowValidator(args.data_dir)

    if not validator.load_csvs():
        print("❌ Failed to load CSV files")
        sys.exit(1)

    print(f"\nData directory: {validator.data_dir}")
    print(f"Validation mode: {args.mode}")

    print("\nCSV Files Loaded:")
    print(f"  - ideas_inbox.csv: {len(validator.ideas)} rows")
    print(f"  - ideas_research.csv: {len(validator.research)} rows")
    print(f"  - posts_content.csv: {len(validator.posts)} rows")

    success = True

    # Schema validation
    success &= validator.validate_csv_schemas()
    success &= validator.validate_numeric_fields()

    # Mode-specific validation
    if args.mode in ['text', 'both']:
        success &= validator.validate_text_mode()

    if args.mode in ['routine', 'both']:
        success &= validator.validate_routine_mode()

    # Print report
    validator.print_report()

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
