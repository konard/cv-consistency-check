"""Tests for CV comparator."""

import pytest
from cv_checker.models import CVData
from cv_checker.comparator import CVComparator


class TestCVComparator:
    """Tests for CVComparator class."""

    def test_normalize_string(self):
        """Test string normalization."""
        assert CVComparator.normalize_string("  Hello World  ") == "hello world"
        assert CVComparator.normalize_string("Test") == "test"
        assert CVComparator.normalize_string("") is None
        assert CVComparator.normalize_string(None) is None

    def test_are_values_consistent_both_none(self):
        """Test consistency check with both values None."""
        assert CVComparator.are_values_consistent(None, None) is True

    def test_are_values_consistent_one_none(self):
        """Test consistency check with one value None."""
        assert CVComparator.are_values_consistent("value", None) is True
        assert CVComparator.are_values_consistent(None, "value") is True

    def test_are_values_consistent_equal(self):
        """Test consistency check with equal values."""
        assert CVComparator.are_values_consistent("Test", "test") is True
        assert CVComparator.are_values_consistent("  Trimmed  ", "trimmed") is True

    def test_are_values_consistent_different(self):
        """Test consistency check with different values."""
        assert CVComparator.are_values_consistent("value1", "value2") is False

    def test_compare_identical_cvs(self):
        """Test comparing identical CVs."""
        cv1 = CVData(
            name="John Doe",
            bio="Developer",
            location="NYC",
            company="TechCo",
            website="https://example.com",
            email="john@example.com"
        )
        cv2 = CVData(
            name="John Doe",
            bio="Developer",
            location="NYC",
            company="TechCo",
            website="https://example.com",
            email="john@example.com"
        )

        comparator = CVComparator()
        results = comparator.compare(cv1, cv2)

        assert len(results) == 6
        assert all(r.is_consistent for r in results)

    def test_compare_different_cvs(self):
        """Test comparing different CVs."""
        cv1 = CVData(
            name="John Doe",
            location="New York"
        )
        cv2 = CVData(
            name="Jane Smith",
            location="San Francisco"
        )

        comparator = CVComparator()
        results = comparator.compare(cv1, cv2)

        name_result = next(r for r in results if r.field_name == "Name")
        location_result = next(r for r in results if r.field_name == "Location")

        assert name_result.is_consistent is False
        assert location_result.is_consistent is False

    def test_compare_partial_cvs(self):
        """Test comparing CVs with some missing data."""
        cv1 = CVData(
            name="John Doe",
            location="NYC"
        )
        cv2 = CVData(
            name="John Doe",
            bio="Developer"
        )

        comparator = CVComparator()
        results = comparator.compare(cv1, cv2)

        name_result = next(r for r in results if r.field_name == "Name")
        location_result = next(r for r in results if r.field_name == "Location")
        bio_result = next(r for r in results if r.field_name == "Bio")

        assert name_result.is_consistent is True
        assert location_result.is_consistent is True  # One has data, one doesn't
        assert bio_result.is_consistent is True  # One has data, one doesn't

    def test_generate_report(self):
        """Test report generation."""
        cv1 = CVData(name="John Doe", location="NYC")
        cv2 = CVData(name="Jane Smith", location="NYC")

        comparator = CVComparator()
        results = comparator.compare(cv1, cv2)
        report = comparator.generate_report(results, "GitHub", "Stack Overflow")

        assert "GitHub" in report
        assert "Stack Overflow" in report
        assert "CV Consistency Check" in report
        assert "John Doe" in report
        assert "Jane Smith" in report

    def test_generate_report_all_consistent(self):
        """Test report generation with all consistent data."""
        cv1 = CVData(name="John Doe")
        cv2 = CVData(name="John Doe")

        comparator = CVComparator()
        results = comparator.compare(cv1, cv2)
        report = comparator.generate_report(results)

        assert "All comparable fields are consistent" in report
        assert "✓" in report

    def test_generate_report_with_inconsistencies(self):
        """Test report generation with inconsistencies."""
        cv1 = CVData(name="John", location="NYC")
        cv2 = CVData(name="Jane", location="SF")

        comparator = CVComparator()
        results = comparator.compare(cv1, cv2)
        report = comparator.generate_report(results)

        assert "INCONSISTENCIES FOUND" in report
        assert "✗" in report
