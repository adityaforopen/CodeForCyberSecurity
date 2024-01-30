# web_scraping.py

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    print(f"Scraping website: {url}")
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Example: Extracting text from all <p> tags
            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                print(paragraph.text)
        else:
            print("Failed to fetch webpage:", response.status_code)
    except Exception as e:
        print(f"Error scraping website: {e}")

if __name__ == "__main__":
    url = input("Enter URL of the website to scrape: ")
    scrape_website(url)
