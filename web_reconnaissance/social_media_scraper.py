# social_media_scraping.py

import requests
from bs4 import BeautifulSoup

def scrape_social_media(url):
    print(f"Scraping social media site: {url}")
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Example: Extracting text from all <div> tags with class="post"
            posts = soup.find_all('div', class_='post')
            for post in posts:
                print(post.text)
        else:
            print("Failed to fetch webpage:", response.status_code)
    except Exception as e:
        print(f"Error scraping social media site: {e}")

if __name__ == "__main__":
    url = input("Enter URL of the social media site to scrape: ")
    scrape_social_media(url)
