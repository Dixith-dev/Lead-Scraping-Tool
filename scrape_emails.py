from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

def append_emails_to_file(emails, output_file):
    """Appends emails to the output file as they are found."""
    with open(output_file, 'a') as file:
        for email in emails:
            file.write(email + '\n')

def find_emails_on_website(url, driver, output_file):
    """Uses Selenium to navigate to a website, find emails, and append them to a file."""
    try:
        driver.get(url)
        time.sleep(5)  # Wait for JavaScript to load content
        page_source = driver.page_source
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        emails = set(re.findall(email_pattern, page_source))
        if emails:
            append_emails_to_file(emails, output_file)
    except Exception as e:
        print(f"Error accessing {url}: {e}")

def main(input_file, output_file):
    """Reads URLs, extracts emails using Selenium, and appends them to a file."""
    options = webdriver.ChromeOptions()
    options.headless = True  # Run browser in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    with open(output_file, 'w') as f:
        f.write('')  # Clear the file at the start
    
    with open(input_file, 'r') as urls_file:
        for url in urls_file:
            url = url.strip()
            if url and not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            find_emails_on_website(url, driver, output_file)

    driver.quit()  # Close the browser session

if __name__ == "__main__":
    main('real_estate_leads.txt', 'emails_found.txt')