# Import libraries
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import csv

# Function for web scraping


def web_scrape():
    # Try-Catch block for error handling
    try:
        # Define the URL to scrape - Python job listing website
        URL = "https://realpython.github.io/fake-jobs/"

        # Send a GET request to the URL - Retrieves the correct URL
        page = requests.get(URL)

        # Raise an exception for any HTTP or other errors
        page.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup - Analyse and extract the HTML data
        soup = BeautifulSoup(page.content, "html.parser")

        # Find the container for job results within the HTML
        results = soup.find(id="ResultsContainer")

        # Find all job elements within the container
        job_elements = results.find_all("div", class_="card-content")

        # Initialize a list to store job data that we want to extract
        job_data = []

        # Loop through each job element from the HTML and extract relevant data
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")

            # Append job data as a dictionary to the list - matching the title, company, location with relevant data
            job_data.append({
                "Title": title_element.text.strip(),
                "Company": company_element.text.strip(),
                "Location": location_element.text.strip()
            })

        # Print a success message
        print("Successfully scraped data from", URL)

        # Return the collected job data as a list of dictionaries - Used for the csv writing function
        return job_data

    # Handle all exceptions, including RequestException and AttributeError
    except (RequestException, AttributeError) as error:
        print("There is an Error:", error)

# Function to write job data to a CSV file


def write_csv(job_data):
    # Open a new CSV file for writing - Imported CSV library earlier for this
    with open("jobData.csv", "w", newline="", encoding="utf-8") as jobCsv:
        # Create a CSV writer with specified fieldnames - These will be the header row
        writer = csv.DictWriter(
            jobCsv, fieldnames=["Title", "Company", "Location"])

        # Write the CSV header row with column names
        writer.writeheader()

        # Write the job data rows to the CSV file - Following the fieldnames format
        writer.writerows(job_data)


# Main program
if __name__ == "__main__":
    # Scrape job data using the web_scrape function
    scraped_data = web_scrape()

    # Write the scraped data to a CSV file using the write_csv function
    write_csv(scraped_data)

    # Print a success message
    print("Data has been written to jobData.csv")

# Rakhin Amin
