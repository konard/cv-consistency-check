import { CVData } from './types';

export interface Scraper {
  scrape(url: string): Promise<CVData>;
}

export abstract class BaseScraper implements Scraper {
  abstract scrape(url: string): Promise<CVData>;

  protected async initBrowser() {
    const { chromium } = require('playwright');
    return await chromium.launch();
  }
}