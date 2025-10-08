# cv-consistency-check
A checker to help employee to keep all their CVs/resumes in sync

## Prototype

This is a prototype that compares CVs from different platforms like HH.ru and StackOverflow.

### Features

- Scrapes basic information (name, position, location, skills) from CV profiles
- Compares data between two platforms
- Identifies matches and differences

### Usage

```bash
npm install
npm run build
npm start
```

The prototype currently uses mock data for demonstration. To use with real URLs, modify `src/index.ts` with actual CV URLs.

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

- Support for more platforms (LinkedIn, Habr Career, etc.)
- API-based fetching where available
- More detailed comparison (experience, education)
- Web interface
- Automated syncing suggestions
