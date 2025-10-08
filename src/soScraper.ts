import { BaseScraper } from './scraper';
import { CVData } from './types';

export class SOFScraper extends BaseScraper {
  async scrape(url: string): Promise<CVData> {
    const browser = await this.initBrowser();
    const page = await browser.newPage();

    try {
      await page.goto(url, { waitUntil: 'networkidle' });

      // Wait for content to load
      await page.waitForTimeout(2000);

      const data: CVData = {};

      // Extract name
      try {
        data.name = await page.locator('h2.mb0').textContent();
      } catch (e) {
        console.log('Name not found');
      }

      // Extract location
      try {
        data.location = await page.locator('.fc-medium.fs-body2').first().textContent();
      } catch (e) {
        console.log('Location not found');
      }

      // Extract position/title (from profile description or job title if available)
      try {
        const title = await page.locator('.fs-title').first().textContent();
        if (title) data.position = title.trim();
      } catch (e) {
        console.log('Position not found');
      }

      // Extract top tags as skills
      try {
        const tags = await page.locator('.post-tag').allTextContents();
        data.skills = tags.slice(0, 10); // Top 10 tags
      } catch (e) {
        console.log('Tags not found');
      }

      return data;
    } finally {
      await browser.close();
    }
  }
}