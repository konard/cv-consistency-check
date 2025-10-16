"""Comparator for CV data from different platforms."""

from typing import List, Optional
from .models import CVData, ComparisonResult


class CVComparator:
    """Compares CV data from different platforms."""

    @staticmethod
    def normalize_string(value: Optional[str]) -> Optional[str]:
        """
        Normalize a string for comparison.

        Args:
            value: String to normalize

        Returns:
            Normalized string or None
        """
        if not value:
            return None
        return value.strip().lower()

    @staticmethod
    def are_values_consistent(value1: Optional[str], value2: Optional[str]) -> bool:
        """
        Check if two values are consistent.

        Args:
            value1: First value
            value2: Second value

        Returns:
            True if values are consistent (equal or one is None), False otherwise
        """
        # If both are None or empty, consider them consistent
        if not value1 and not value2:
            return True

        # If one is None but the other isn't, they're still consistent
        # (just means one platform doesn't have that info)
        if not value1 or not value2:
            return True

        # Normalize and compare
        norm1 = CVComparator.normalize_string(value1)
        norm2 = CVComparator.normalize_string(value2)

        return norm1 == norm2

    def compare(self, cv1: CVData, cv2: CVData, platform1_name: str = "Platform 1",
                platform2_name: str = "Platform 2") -> List[ComparisonResult]:
        """
        Compare two CV data objects.

        Args:
            cv1: First CV data
            cv2: Second CV data
            platform1_name: Name of first platform (for reporting)
            platform2_name: Name of second platform (for reporting)

        Returns:
            List of comparison results
        """
        results = []

        # Compare each field
        fields = [
            ("name", cv1.name, cv2.name),
            ("bio", cv1.bio, cv2.bio),
            ("location", cv1.location, cv2.location),
            ("company", cv1.company, cv2.company),
            ("website", cv1.website, cv2.website),
            ("email", cv1.email, cv2.email)
        ]

        for field_name, value1, value2 in fields:
            is_consistent = self.are_values_consistent(value1, value2)
            results.append(ComparisonResult(
                field_name=field_name.capitalize(),
                platform1_value=value1,
                platform2_value=value2,
                is_consistent=is_consistent
            ))

        return results

    @staticmethod
    def generate_report(results: List[ComparisonResult], platform1_name: str = "Platform 1",
                       platform2_name: str = "Platform 2") -> str:
        """
        Generate a human-readable report from comparison results.

        Args:
            results: List of comparison results
            platform1_name: Name of first platform
            platform2_name: Name of second platform

        Returns:
            Formatted report string
        """
        report_lines = [
            f"\n{'=' * 60}",
            f"CV Consistency Check: {platform1_name} vs {platform2_name}",
            f"{'=' * 60}\n"
        ]

        inconsistencies = [r for r in results if not r.is_consistent]
        consistent_count = len(results) - len(inconsistencies)

        report_lines.append(f"Summary: {consistent_count}/{len(results)} fields are consistent\n")

        if inconsistencies:
            report_lines.append("⚠️  INCONSISTENCIES FOUND:\n")
            for result in inconsistencies:
                report_lines.append(f"  {result.field_name}:")
                report_lines.append(f"    {platform1_name}: {result.platform1_value or 'N/A'}")
                report_lines.append(f"    {platform2_name}: {result.platform2_value or 'N/A'}")
                report_lines.append("")
        else:
            report_lines.append("✓ All comparable fields are consistent!")

        report_lines.append("\nDetailed Comparison:")
        report_lines.append("-" * 60)
        for result in results:
            status = "✓" if result.is_consistent else "✗"
            report_lines.append(f"\n{status} {result.field_name}:")
            report_lines.append(f"  {platform1_name}: {result.platform1_value or 'N/A'}")
            report_lines.append(f"  {platform2_name}: {result.platform2_value or 'N/A'}")

        report_lines.append("\n" + "=" * 60)
        return "\n".join(report_lines)
