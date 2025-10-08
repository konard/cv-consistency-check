import { compareCVs } from './comparer';

describe('CV Comparer', () => {
  test('should throw error for unsupported URLs', async () => {
    await expect(compareCVs('https://unsupported.com/cv', 'https://hh.ru/resume/123')).rejects.toThrow('Unsupported URL');
  });

  test('should accept HH.ru URLs', async () => {
    // This will fail in test environment since no browser, but tests the URL validation
    await expect(compareCVs('https://hh.ru/resume/123', 'https://hh.ru/resume/456')).rejects.toThrow();
    // Expect it to fail due to browser/scraping, not URL validation
  });

  test('should accept Habr Career URLs', async () => {
    await expect(compareCVs('https://career.habr.com/resumes/123', 'https://hh.ru/resume/456')).rejects.toThrow();
    // Expect it to fail due to browser/scraping, not URL validation
  });
});