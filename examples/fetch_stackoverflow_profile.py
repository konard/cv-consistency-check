#!/usr/bin/env python3
"""
Example script to fetch and display a Stack Overflow profile.

Usage:
    python examples/fetch_stackoverflow_profile.py <stackoverflow_user_id>

Example:
    python examples/fetch_stackoverflow_profile.py 22656
"""

import sys
import os

# Add parent directory to path to import cv_checker
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cv_checker.fetchers import StackOverflowFetcher


def main():
    """Main function to fetch and display Stack Overflow profile."""
    if len(sys.argv) != 2:
        print("Usage: python fetch_stackoverflow_profile.py <stackoverflow_user_id>")
        print("\nExample:")
        print("  python fetch_stackoverflow_profile.py 22656")
        print("\nNote: You need the numeric user ID from Stack Overflow URL")
        print("      (e.g., https://stackoverflow.com/users/22656/jon-skeet)")
        sys.exit(1)

    user_id = sys.argv[1]
    fetcher = StackOverflowFetcher()

    print(f"Fetching Stack Overflow profile for user ID: {user_id}")
    print("-" * 60)

    try:
        cv_data = fetcher.fetch(user_id)
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
