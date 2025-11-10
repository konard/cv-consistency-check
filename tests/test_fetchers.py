"""Tests for CV fetchers."""

import pytest
from unittest.mock import Mock, patch
from cv_checker.fetchers import GitHubFetcher, StackOverflowFetcher
from cv_checker.models import CVData


class TestGitHubFetcher:
    """Tests for GitHubFetcher class."""

    @patch('cv_checker.fetchers.requests.get')
    def test_fetch_github_profile(self, mock_get):
        """Test fetching a GitHub profile."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "name": "John Doe",
            "bio": "Software Developer",
            "location": "San Francisco, CA",
            "company": "GitHub",
            "blog": "https://johndoe.dev",
            "email": "john@example.com",
            "html_url": "https://github.com/johndoe"
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        fetcher = GitHubFetcher()
        cv_data = fetcher.fetch("johndoe")

        assert cv_data.name == "John Doe"
        assert cv_data.bio == "Software Developer"
        assert cv_data.location == "San Francisco, CA"
        assert cv_data.company == "GitHub"
        assert cv_data.website == "https://johndoe.dev"
        assert cv_data.email == "john@example.com"

        mock_get.assert_called_once_with(
            "https://api.github.com/users/johndoe",
            timeout=10
        )

    @patch('cv_checker.fetchers.requests.get')
    def test_fetch_github_profile_minimal(self, mock_get):
        """Test fetching a GitHub profile with minimal data."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "name": "Jane",
            "html_url": "https://github.com/jane"
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        fetcher = GitHubFetcher()
        cv_data = fetcher.fetch("jane")

        assert cv_data.name == "Jane"
        assert cv_data.bio is None
        assert cv_data.website == "https://github.com/jane"

    @patch('cv_checker.fetchers.requests.get')
    def test_fetch_github_profile_uses_html_url_fallback(self, mock_get):
        """Test that html_url is used when blog is empty."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "name": "Test User",
            "blog": "",
            "html_url": "https://github.com/testuser"
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        fetcher = GitHubFetcher()
        cv_data = fetcher.fetch("testuser")

        assert cv_data.website == "https://github.com/testuser"


class TestStackOverflowFetcher:
    """Tests for StackOverflowFetcher class."""

    @patch('cv_checker.fetchers.requests.get')
    def test_fetch_stackoverflow_profile(self, mock_get):
        """Test fetching a Stack Overflow profile."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "items": [{
                "display_name": "John Doe",
                "location": "San Francisco",
                "website_url": "https://johndoe.dev"
            }]
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        fetcher = StackOverflowFetcher()
        cv_data = fetcher.fetch("123456")

        assert cv_data.name == "John Doe"
        assert cv_data.location == "San Francisco"
        assert cv_data.website == "https://johndoe.dev"
        assert cv_data.bio is None  # Not available in SO API
        assert cv_data.company is None  # Not available in SO API
        assert cv_data.email is None  # Not public in SO API

        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert "https://api.stackexchange.com/2.3/users/123456" in call_args[0]

    @patch('cv_checker.fetchers.requests.get')
    def test_fetch_stackoverflow_profile_not_found(self, mock_get):
        """Test fetching a non-existent Stack Overflow profile."""
        mock_response = Mock()
        mock_response.json.return_value = {"items": []}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        fetcher = StackOverflowFetcher()

        with pytest.raises(ValueError, match="No user found with ID"):
            fetcher.fetch("999999")

    @patch('cv_checker.fetchers.requests.get')
    def test_fetch_stackoverflow_profile_minimal(self, mock_get):
        """Test fetching a Stack Overflow profile with minimal data."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "items": [{
                "display_name": "Jane"
            }]
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        fetcher = StackOverflowFetcher()
        cv_data = fetcher.fetch("123")

        assert cv_data.name == "Jane"
        assert cv_data.location is None
        assert cv_data.website is None
