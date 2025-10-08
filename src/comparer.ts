import { CVData, ComparisonResult } from './types';
import { HHScraper } from './hhScraper';
import { HabrScraper } from './habrScraper';

export async function compareCVs(url1: string, url2: string): Promise<ComparisonResult> {
  const hhScraper = new HHScraper();
  const habrScraper = new HabrScraper();

  // Determine which scraper to use based on URL
  const getScraper = (url: string) => {
    if (url.includes('hh.ru')) return hhScraper;
    if (url.includes('career.habr.com')) return habrScraper;
    throw new Error(`Unsupported URL: ${url}. Currently supports hh.ru and career.habr.com`);
  };

  const scraper1 = getScraper(url1);
  const scraper2 = getScraper(url2);

  const [data1, data2] = await Promise.all([
    scraper1.scrape(url1),
    scraper2.scrape(url2)
  ]);

  const differences: { [key: string]: { value1: any; value2: any } } = {};
  const matches: { [key: string]: any } = {};

  const keys = new Set([...Object.keys(data1), ...Object.keys(data2)]);

  for (const key of keys) {
    const value1 = (data1 as any)[key];
    const value2 = (data2 as any)[key];

    if (value1 === value2) {
      matches[key] = value1;
    } else {
      differences[key] = { value1, value2 };
    }
  }

  return {
    platform1: data1,
    platform2: data2,
    differences,
    matches
  };
}