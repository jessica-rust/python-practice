# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# import csv

# def decode_cfemail(cfemail):
#     r = int(cfemail[:2], 16)
#     email = ''.join(
#         chr(int(cfemail[i:i+2], 16) ^ r) for i in range(2, len(cfemail), 2)
#     )
#     return email

# BASE_URL = "https://greensourcedfw.org/greenbusiness"
# headers = {"User-Agent": "Mozilla/5.0"}

# res = requests.get(BASE_URL, headers=headers)
# soup = BeautifulSoup(res.text, "html.parser")

# business_tag = soup.find_all(class_ = "views-field views-field-field-business-categories")
# business = business_tag.get_text().strip() if business_tag else None

# print(business)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Setup paths ===
CHROME_PATH = "C:/Users/Jessi/Downloads/chrome-win64/chrome-win64/chrome.exe"
CHROMEDRIVER_PATH = "C:/Users/Jessi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

options = Options()
options.binary_location = CHROME_PATH
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

try:
    url = "https://www.greenbusinessnetwork.org/directory#!biz/id/673e67c554150f20d701d775"
    print(f"Opening page: {url}")
    driver.get(url)

    # Wait for the element with the website link to appear
    website_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "SFbizctcweb")))

    # Get the href attribute and text content
    website_link = website_element.get_attribute("href")
    website_text = website_element.text

    print(f"Website href attribute: {website_link}")
    print(f"Website text: {website_text}")

except Exception as e:
    print(f"Error finding website link: {e}")

finally:
    driver.quit()