import { compareCVs } from './comparer';

async function main() {
  // For prototype testing, use mock data since finding real public CV URLs is hard
  // In production, these would be real URLs
  const mockData1 = {
    name: 'John Doe',
    position: 'Software Developer',
    location: 'Moscow, Russia',
    skills: ['JavaScript', 'TypeScript', 'React']
  };

  const mockData2 = {
    name: 'John Doe',
    position: 'Senior Software Developer',
    location: 'Moscow, Russia',
    skills: ['JavaScript', 'Python', 'React']
  };

  // Simulate comparison
  const differences: { [key: string]: { value1: any; value2: any } } = {};
  const matches: { [key: string]: any } = {};

  const keys = new Set([...Object.keys(mockData1), ...Object.keys(mockData2)]);

  for (const key of keys) {
    const value1 = (mockData1 as any)[key];
    const value2 = (mockData2 as any)[key];

    if (JSON.stringify(value1) === JSON.stringify(value2)) {
      matches[key] = value1;
    } else {
      differences[key] = { value1, value2 };
    }
  }

  const result = {
    platform1: mockData1,
    platform2: mockData2,
    differences,
    matches
  };

  console.log('CV Comparison Result (Prototype with Mock Data):');
  console.log(JSON.stringify(result, null, 2));

  // Uncomment below for real scraping (requires real URLs)
  /*
  const hhUrl = 'https://hh.ru/resume/...'; // real HH.ru resume URL
  const soUrl = 'https://stackoverflow.com/users/12345/username'; // real SO user URL

  try {
    const realResult = await compareCVs(hhUrl, soUrl);
    console.log('Real CV Comparison Result:');
    console.log(JSON.stringify(realResult, null, 2));
  } catch (error) {
    console.error('Error:', error);
  }
  */
}

main();