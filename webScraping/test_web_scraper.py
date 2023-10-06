import unittest
import requests
from web_scraper import web_scrape  # Import your web_scrape function


class TestWebScrape(unittest.TestCase):

    def test_url_parsing(self):
        # Define a URL for testing (modify as needed)
        test_url = "https://realpython.github.io/fake-jobs/"

        # Call the web_scrape function with the test URL
        web_scrape()

        # Use requests to make a GET request to the URL
        response = requests.get(test_url)

        # Assert that the page URL from the response matches the test URL
        self.assertEqual(web_scrape.page.url, test_url)


if __name__ == '__main__':
    unittest.main()
