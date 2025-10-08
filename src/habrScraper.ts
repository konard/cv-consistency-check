import { BaseScraper } from './scraper';
import { CVData } from './types';

export class HabrScraper extends BaseScraper {
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
        data.name = await page.locator('.resume-header__name').textContent();
      } catch (e) {
        console.log('Name not found');
      }

      // Extract position
      try {
        data.position = await page.locator('.resume-header__position').textContent();
      } catch (e) {
        console.log('Position not found');
      }

      // Extract location
      try {
        data.location = await page.locator('.resume-header__location').textContent();
      } catch (e) {
        console.log('Location not found');
      }

      // Extract skills
      try {
        const skills = await page.locator('.skill-item__name').allTextContents();
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