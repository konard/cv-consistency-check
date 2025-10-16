#!/usr/bin/env python3
"""
Example script demonstrating CV comparison between GitHub and Stack Overflow.

Usage:
    python examples/compare_github_stackoverflow.py <github_username> <stackoverflow_user_id>

Example:
    python examples/compare_github_stackoverflow.py torvalds 22656
"""

import sys
import os

# Add parent directory to path to import cv_checker
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cv_checker.fetchers import GitHubFetcher, StackOverflowFetcher
from cv_checker.comparator import CVComparator


def main():
    """Main function to compare GitHub and Stack Overflow profiles."""
    if len(sys.argv) != 3:
        print("Usage: python compare_github_stackoverflow.py <github_username> <stackoverflow_user_id>")
        print("\nExample:")
        print("  python compare_github_stackoverflow.py torvalds 22656")
        sys.exit(1)

    github_username = sys.argv[1]
    stackoverflow_id = sys.argv[2]

    print(f"Fetching GitHub profile for: {github_username}")
    github_fetcher = GitHubFetcher()

    try:
        github_cv = github_fetcher.fetch(github_username)
        print("✓ GitHub profile fetched successfully\n")
        print("GitHub Profile:")
        print(github_cv)
        print()
    except Exception as e:
        print(f"✗ Error fetching GitHub profile: {e}")
        sys.exit(1)

    print(f"Fetching Stack Overflow profile for user ID: {stackoverflow_id}")
    stackoverflow_fetcher = StackOverflowFetcher()

    try:
        stackoverflow_cv = stackoverflow_fetcher.fetch(stackoverflow_id)
        print("✓ Stack Overflow profile fetched successfully\n")
        print("Stack Overflow Profile:")
        print(stackoverflow_cv)
        print()
    except Exception as e:
        print(f"✗ Error fetching Stack Overflow profile: {e}")
        sys.exit(1)

    print("Comparing profiles...\n")
    comparator = CVComparator()
    results = comparator.compare(github_cv, stackoverflow_cv)

    report = comparator.generate_report(results, "GitHub", "Stack Overflow")
    print(report)

    # Exit with error code if inconsistencies found
    inconsistencies = [r for r in results if not r.is_consistent]
    if inconsistencies:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
