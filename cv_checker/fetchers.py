"""Fetchers for different CV platforms."""

import requests
from abc import ABC, abstractmethod
from typing import Optional
from .models import CVData


class CVFetcher(ABC):
    """Abstract base class for CV fetchers."""

    @abstractmethod
    def fetch(self, username: str) -> CVData:
        """Fetch CV data for a given username."""
        pass


class GitHubFetcher(CVFetcher):
    """Fetcher for GitHub profiles."""

    API_URL = "https://api.github.com/users/{username}"

    def fetch(self, username: str) -> CVData:
        """
        Fetch CV data from GitHub profile.

        Args:
            username: GitHub username

        Returns:
            CVData object with profile information

        Raises:
            requests.HTTPError: If the API request fails
        """
        url = self.API_URL.format(username=username)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        return CVData(
            name=data.get("name"),
            bio=data.get("bio"),
            location=data.get("location"),
            company=data.get("company"),
            website=data.get("blog") or data.get("html_url"),
            email=data.get("email")
        )


class StackOverflowFetcher(CVFetcher):
    """Fetcher for Stack Overflow profiles."""

    API_URL = "https://api.stackexchange.com/2.3/users/{user_id}"

    def fetch(self, user_id: str) -> CVData:
        """
        Fetch CV data from Stack Overflow profile.

        Args:
            user_id: Stack Overflow user ID

        Returns:
            CVData object with profile information

        Raises:
            requests.HTTPError: If the API request fails
        """
        url = self.API_URL.format(user_id=user_id)
        params = {
            "site": "stackoverflow",
            "filter": "!9YdnSIN*P"  # Includes more profile details
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data.get("items"):
            raise ValueError(f"No user found with ID: {user_id}")

        user = data["items"][0]

        return CVData(
            name=user.get("display_name"),
            bio=None,  # Stack Overflow API doesn't provide bio in this endpoint
            location=user.get("location"),
            company=None,  # Not readily available in Stack Overflow API
            website=user.get("website_url"),
            email=None  # Not public in Stack Overflow API
        )
