"""Tests for data models."""

import pytest
from cv_checker.models import CVData, ComparisonResult


class TestCVData:
    """Tests for CVData model."""

    def test_cvdata_creation(self):
        """Test creating a CVData object."""
        cv = CVData(
            name="John Doe",
            bio="Software Engineer",
            location="San Francisco, CA",
            company="Tech Corp",
            website="https://example.com",
            email="john@example.com"
        )

        assert cv.name == "John Doe"
        assert cv.bio == "Software Engineer"
        assert cv.location == "San Francisco, CA"
        assert cv.company == "Tech Corp"
        assert cv.website == "https://example.com"
        assert cv.email == "john@example.com"

    def test_cvdata_repr_with_all_fields(self):
        """Test CVData representation with all fields."""
        cv = CVData(
            name="Jane Smith",
            bio="Developer",
            location="NYC",
            company="StartupCo",
            website="https://jane.dev",
            email="jane@example.com"
        )

        repr_str = repr(cv)
        assert "Name: Jane Smith" in repr_str
        assert "Bio: Developer" in repr_str
        assert "Location: NYC" in repr_str
        assert "Company: StartupCo" in repr_str
        assert "Website: https://jane.dev" in repr_str
        assert "Email: jane@example.com" in repr_str

    def test_cvdata_repr_with_long_bio(self):
        """Test CVData representation with long bio truncation."""
        long_bio = "a" * 100
        cv = CVData(name="Test", bio=long_bio)

        repr_str = repr(cv)
        assert "..." in repr_str
        assert len(long_bio) > 50

    def test_cvdata_repr_empty(self):
        """Test CVData representation with no data."""
        cv = CVData()
        assert repr(cv) == "No data available"


class TestComparisonResult:
    """Tests for ComparisonResult model."""

    def test_comparison_result_consistent(self):
        """Test ComparisonResult with consistent values."""
        result = ComparisonResult(
            field_name="Name",
            platform1_value="John Doe",
            platform2_value="John Doe",
            is_consistent=True
        )

        assert result.field_name == "Name"
        assert result.is_consistent is True
        repr_str = repr(result)
        assert "✓ Consistent" in repr_str

    def test_comparison_result_inconsistent(self):
        """Test ComparisonResult with inconsistent values."""
        result = ComparisonResult(
            field_name="Location",
            platform1_value="New York",
            platform2_value="San Francisco",
            is_consistent=False
        )

        assert result.is_consistent is False
        repr_str = repr(result)
        assert "✗ Inconsistent" in repr_str
        assert "New York" in repr_str
        assert "San Francisco" in repr_str

    def test_comparison_result_with_none(self):
        """Test ComparisonResult with None values."""
        result = ComparisonResult(
            field_name="Email",
            platform1_value=None,
            platform2_value="test@example.com",
            is_consistent=True
        )

        repr_str = repr(result)
        assert "N/A" in repr_str
        assert "test@example.com" in repr_str
