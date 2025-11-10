"""Data models for CV information."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CVData:
    """Represents basic CV/profile information."""

    name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    website: Optional[str] = None
    email: Optional[str] = None

    def __repr__(self) -> str:
        """Return a readable representation of CV data."""
        fields = []
        if self.name:
            fields.append(f"Name: {self.name}")
        if self.bio:
            fields.append(f"Bio: {self.bio[:50]}..." if len(self.bio) > 50 else f"Bio: {self.bio}")
        if self.location:
            fields.append(f"Location: {self.location}")
        if self.company:
            fields.append(f"Company: {self.company}")
        if self.website:
            fields.append(f"Website: {self.website}")
        if self.email:
            fields.append(f"Email: {self.email}")

        return "\n".join(fields) if fields else "No data available"


@dataclass
class ComparisonResult:
    """Represents the result of comparing two CVs."""

    field_name: str
    platform1_value: Optional[str]
    platform2_value: Optional[str]
    is_consistent: bool

    def __repr__(self) -> str:
        """Return a readable representation of comparison result."""
        status = "✓ Consistent" if self.is_consistent else "✗ Inconsistent"
        return (f"{self.field_name}: {status}\n"
                f"  Platform 1: {self.platform1_value or 'N/A'}\n"
                f"  Platform 2: {self.platform2_value or 'N/A'}")
