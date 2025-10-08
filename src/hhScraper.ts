import { BaseScraper } from './scraper';
import { CVData } from './types';

export class HHScraper extends BaseScraper {
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
        data.name = await page.locator('h2[data-qa="resume-personal-name"]').textContent();
      } catch (e) {
        console.log('Name not found');
      }

      // Extract position
      try {
        data.position = await page.locator('span[data-qa="resume-block-title-position"]').textContent();
      } catch (e) {
        console.log('Position not found');
      }

      // Extract location
      try {
        data.location = await page.locator('span[data-qa="resume-personal-address"]').textContent();
      } catch (e) {
        console.log('Location not found');
      }

      // Extract skills
      try {
        const skills = await page.locator('span[data-qa="bloko-tag__text"]').allTextContents();
        data.skills = skills.filter((skill: string) => skill.trim().length > 0);
      } catch (e) {
        console.log('Skills not found');
      }

      return data;
    } finally {
      await browser.close();
    }
  }
}