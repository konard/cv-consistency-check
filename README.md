# cv-consistency-check
A checker to help employee to keep all their CVs/resumes in sync

## Prototype

This is a prototype that compares CVs from different platforms like HH.ru and Habr Career.

### Features

- Scrapes basic information (name, position, location, skills) from CV profiles
- Compares data between two platforms
- Identifies matches and differences
- Environment variable support for configuration

### Usage

```bash
npm install
npm run build
npm start
```

Create a `.env` file based on `.env.example` to provide CV URLs:

```bash
cp .env.example .env
# Edit .env with your CV URLs
npm start
```

The prototype currently uses mock data for demonstration if no URLs are provided.

### Supported Platforms

- HH.ru (hh.ru)
- Habr Career (career.habr.com)

### Example Output

```
CV Comparison Result (Prototype with Mock Data):
{
  "platform1": {
    "name": "John Doe",
    "position": "Software Developer",
    "location": "Moscow, Russia",
    "skills": ["JavaScript", "TypeScript", "React"]
  },
  "platform2": {
    "name": "John Doe",
    "position": "Senior Software Developer",
    "location": "Moscow, Russia",
    "skills": ["JavaScript", "Python", "React"]
  },
  "differences": {
    "position": {
      "value1": "Software Developer",
      "value2": "Senior Software Developer"
    },
    "skills": {
      "value1": ["JavaScript", "TypeScript", "React"],
      "value2": ["JavaScript", "Python", "React"]
    }
  },
  "matches": {
    "name": "John Doe",
    "location": "Moscow, Russia"
  }
}
```

### Future Enhancements

- Support for more platforms (LinkedIn, etc.)
- API-based fetching where available
- More detailed comparison (experience, education)
- Web interface
- Automated syncing suggestions
