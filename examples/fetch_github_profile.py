#!/usr/bin/env python3
"""
Example script to fetch and display a GitHub profile.

Usage:
    python examples/fetch_github_profile.py <github_username>

Example:
    python examples/fetch_github_profile.py torvalds
"""

import sys
import os

# Add parent directory to path to import cv_checker
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cv_checker.fetchers import GitHubFetcher


def main():
    """Main function to fetch and display GitHub profile."""
    if len(sys.argv) != 2:
        print("Usage: python fetch_github_profile.py <github_username>")
        print("\nExample:")
        print("  python fetch_github_profile.py torvalds")
        sys.exit(1)

    username = sys.argv[1]
    fetcher = GitHubFetcher()

    print(f"Fetching GitHub profile for: {username}")
    print("-" * 60)

    try:
        cv_data = fetcher.fetch(username)
        print("\nProfile Information:")
        print("=" * 60)
        print(cv_data)
        print("=" * 60)
        print("\n✓ Profile fetched successfully!")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
