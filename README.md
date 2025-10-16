# cv-consistency-check

A checker to help employees keep all their CVs/resumes in sync across multiple platforms.

## Overview

This tool compares your professional profiles across different platforms (like GitHub, Stack Overflow, LinkedIn, etc.) to ensure consistency in your basic information such as name, bio, location, company, and contact details.

## Features

- **Multi-platform Support**: Currently supports GitHub and Stack Overflow profiles
- **Automated Comparison**: Fetches and compares CV data from different platforms
- **Detailed Reports**: Generates comprehensive reports highlighting inconsistencies
- **Extensible Architecture**: Easy to add support for additional platforms
- **API-based**: Uses official APIs for reliable data fetching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/konard/cv-consistency-check.git
cd cv-consistency-check
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Compare GitHub and Stack Overflow Profiles

```bash
python examples/compare_github_stackoverflow.py <github_username> <stackoverflow_user_id>
```

Example:
```bash
python examples/compare_github_stackoverflow.py torvalds 22656
```

### Fetch Individual Profiles

Fetch GitHub profile:
```bash
python examples/fetch_github_profile.py <github_username>
```

Fetch Stack Overflow profile:
```bash
python examples/fetch_stackoverflow_profile.py <stackoverflow_user_id>
```

## Project Structure

```
cv-consistency-check/
├── cv_checker/           # Main package
│   ├── __init__.py
│   ├── models.py         # Data models (CVData, ComparisonResult)
│   ├── fetchers.py       # Platform-specific fetchers
│   └── comparator.py     # Comparison logic
├── tests/                # Unit tests
│   ├── test_models.py
│   ├── test_fetchers.py
│   └── test_comparator.py
├── examples/             # Example scripts
│   ├── compare_github_stackoverflow.py
│   ├── fetch_github_profile.py
│   └── fetch_stackoverflow_profile.py
├── requirements.txt      # Python dependencies
└── README.md
```

## Development

### Running Tests

```bash
pytest
```

### Adding New Platforms

To add support for a new platform:

1. Create a new fetcher class in `cv_checker/fetchers.py` that inherits from `CVFetcher`
2. Implement the `fetch()` method to retrieve profile data
3. Return a `CVData` object with the extracted information
4. Add tests in `tests/test_fetchers.py`

Example:
```python
class LinkedInFetcher(CVFetcher):
    def fetch(self, profile_id: str) -> CVData:
        # Implement LinkedIn API integration
        pass
```

## Supported Platforms

### Currently Implemented
- **GitHub**: Uses the public GitHub API
- **Stack Overflow**: Uses the Stack Exchange API

### Planned
- LinkedIn
- hh.ru
- career.habr.com
- X (Twitter)
- CodersRank

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This is free and unencumbered software released into the public domain. See [LICENSE](LICENSE) for details.

## Prototype Status

This is currently a prototype implementation demonstrating the core concept of CV consistency checking. The implementation focuses on:
- Basic profile information comparison
- Two platform support (GitHub and Stack Overflow)
- Extensible architecture for adding more platforms
- Comprehensive testing

Future enhancements could include:
- Support for more platforms
- More detailed field comparisons (skills, experience, education)
- Configuration files for custom field mappings
- Web interface
- Automated scheduled checks
- Integration with CI/CD pipelines
