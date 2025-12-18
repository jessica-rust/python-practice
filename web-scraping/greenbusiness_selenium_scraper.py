"""
Project Name: Green Business Network Scraper
Purpose: Scrapes company information from the Green Business Network directory using Selenium, including name, description, location, and website, and saves it to a CSV file
Author: Jessica Rust
Course/Source: Personal Project
Date: 07/27/2025
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# === Setup paths ===
CHROME_PATH = "C:/Users/Jessi/Downloads/chrome-win64/chrome-win64/chrome.exe"
CHROMEDRIVER_PATH = "C:/Users/Jessi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# === Setup Chrome driver options ===
options = Options()
options.binary_location = CHROME_PATH
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless")  # Uncomment if you want headless

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# === Load and scroll the directory page ===
driver.get("https://www.greenbusinessnetwork.org/directory#!directory")
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

cards = driver.find_elements(By.CSS_SELECTOR, "a.SFcrd")
print(f"Found {len(cards)} companies.")

results = []
main_window = driver.current_window_handle

for idx, card in enumerate(cards):
    try:
        name = card.find_element(By.CLASS_NAME, "SFcrdnam").text.strip()
        print(f"\nVisiting: {name}")

        desc_block = card.find_element(By.CLASS_NAME, "SFcrdcnm").text.strip()
        parts = desc_block.split("\n\n")
        description = parts[0].strip() if parts else ""
        location = parts[1].strip() if len(parts) > 1 else ""

        detail_url = card.get_attribute("href")

        # Open detail page in new tab
        driver.execute_script("window.open(arguments[0]);", detail_url)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])

        # Wait specifically for the website link or timeout after 10s
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "SFbizctcweb")))
            website_elem = driver.find_element(By.CLASS_NAME, "SFbizctcweb")
            website = website_elem.get_attribute("href")
        except Exception:
            website = "No website listed"

        # Close tab and return to main window
        driver.close()
        driver.switch_to.window(main_window)

        results.append({
            "Name": name,
            "Description": description,
            "Location": location,
            "Website": website
        })

        time.sleep(1)

    except Exception as e:
        print(f"Skipping problematic company: {name if 'name' in locals() else 'Unknown'} due to error: {e}")
        # Close any extra tabs to avoid stuck tabs
        while len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
        driver.switch_to.window(main_window)
        time.sleep(2)
        continue

# Save results
with open("green_businesses_final.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Description", "Location", "Website"])
    writer.writeheader()
    writer.writerows(results)

driver.quit()