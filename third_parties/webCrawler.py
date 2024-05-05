import requests
from bs4 import BeautifulSoup


def fetch_article_content(url, content_selector='div.caas-body'):
    """
    Fetches and returns the text content from a specified URL using a CSS selector.

    Parameters:
    - url (str): The URL of the webpage to crawl.
    - content_selector (str): The CSS selector to find the content within the page.

    Returns:
    - str: The text content of the article or an error message.
    """
    try:
        # Send a GET request
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

        # Check if the request was successful
        response.raise_for_status()

    except requests.RequestException as e:
        return f"Failed to retrieve the webpage. Error: {e}"

    try:
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main content using the provided CSS selector
        article_content = soup.select_one(content_selector)

        # Return the text within the article content
        if article_content:
            return article_content.get_text(separator="\n", strip=True)
        else:
            return "Content not found. Check your CSS selector."

    except Exception as e:
        return f"An error occurred while parsing the page. Error: {e}"


# Example usage:
url = 'https://finance.yahoo.com/news/heres-1-stock-warren-buffett-202200602.html'
print(fetch_article_content(url))

