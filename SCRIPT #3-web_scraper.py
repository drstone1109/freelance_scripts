""" Web Scraper Script Author: Akshit Description: Scrapes data from any public website and saves it into a clean CSV file. Built as a freelance automation tool. """

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_quotes(url, output_file="scraped_data.csv"):
    """Scrapes quotes from a website and saves to CSV."""

    print(f"\nConnecting to: {url}")

    # Step 1 — Fetch the webpage
    # requests.get() goes to the URL like opening a browser
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    # Check if page loaded successfully (200 = success)
    if response.status_code != 200:
        print(f"Error: Could not reach site. Status: {response.status_code}")
        return

    print("✓ Page loaded successfully")

    # Step 2 — Parse the HTML
    # BeautifulSoup reads the HTML and lets us find elements
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3 — Find the data we want
    # On quotes.toscrape.com each quote is in a div with class "quote"
    quote_blocks = soup.find_all('div', class_='quote')

    print(f"✓ Found {len(quote_blocks)} quotes on page")

    # Step 4 — Extract text from each quote block
    data = []
    for block in quote_blocks:
        quote_text = block.find('span', class_='text').get_text()
        author = block.find('small', class_='author').get_text()
        tags = [t.get_text() for t in block.find_all('a', class_='tag')]
        data.append({
            'Quote': quote_text,
            'Author': author,
            'Tags': ', '.join(tags)
        })

    # Step 5 — Save to CSV using pandas
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

    print(f"✓ Data saved to: {output_file}")
    print(f"✓ Total records: {len(df)}")
    print("\nFirst 3 rows preview:")
    print(df.head(3))

# ---- RUN THE SCRIPT ----
if __name__ == "__main__":
    print("=== Web Scraper v1.0 ===")
    # Test site — safe public site made for scraping practice
    url = "http://quotes.toscrape.com"
    scrape_quotes(url, "quotes_output.csv")