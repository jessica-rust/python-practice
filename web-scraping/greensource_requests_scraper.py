"""
Project Name: GreenSource DFW Scraper
Purpose: Scrapes company data from greensourcedfw.org including name, location, email, website, phone, and business category, and saves it to a CSV file
Author: Jessica Rust
Course/Source: Personal Project
Date: 06/29/2025
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv


def decode_cfemail(cfemail):
    r = int(cfemail[:2], 16)
    email = ''.join(
        chr(int(cfemail[i:i+2], 16) ^ r) for i in range(2, len(cfemail), 2)
    )
    return email


companies = []
BASE_URL = "https://greensourcedfw.org"
url = "/greenbusiness"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}


while url:
	res = requests.get(f"{BASE_URL}{url}", headers=headers)
	print(f"Now scraping {BASE_URL}{url}...")
	soup = BeautifulSoup(res.text, "html.parser")
	company = soup.find_all(class_ = "views-field views-field-title active")


	for info in company:
	    link = info.find("a")
	    if link:
	    	name = link.text.strip()
	    	href = link["href"]
	    	company_url = f"{BASE_URL}{href}"

	    	business = None
	    	row = info.find_parent("tr")
	    	if row:
	    		category_cell = row.select_one("td.views-field.views-field-field-business-categories")
	    		if category_cell:
	    			business = category_cell.get_text(strip=True)

	    	from requests.exceptions import ConnectionError, Timeout
	    	retries = 0
	    	while retries < 3:
	    		try:
	    			sleep(2)  # polite delay
	    			res_2 = requests.get(company_url, headers=headers, timeout=30)
	    			soup_2 = BeautifulSoup(res_2.text, "html.parser")
	    			break  # success, exit loop
	    		except (ConnectionError, Timeout) as e:
	    			print(f"Connection failed for {company_url}. Retrying ({retries + 1}/3)...")
	    			retries += 1
	    			sleep(2)
	    	else:
	    		print(f"Failed to fetch {company_url} after 3 retries. Skipping.")
	    		continue 
	    	
	    	street = soup_2.find("span", itemprop="streetAddress")
	    	city = soup_2.find("span", itemprop="addressLocality")
	    	state = soup_2.find("span", itemprop="addressRegion")
	    	zip_code = soup_2.find("span", itemprop="postalCode")
	    	location_parts = [
	    	street.get_text(strip=True) if street else "",
	    	city.get_text(strip=True) if city else "",
	    	state.get_text(strip=True) if state else "",
	    	zip_code.get_text(strip=True) if zip_code else ""
	    	]
	    	location = ", ".join(part for part in location_parts if part)

	    	
	    	email_span = soup_2.select_one('span.__cf_email__')

	    	email = None

	    	if email_span and email_span.has_attr('data-cfemail'):
	    		encoded = email_span['data-cfemail']
	    		try:
	    			email = decode_cfemail(encoded)
	    		except Exception as e:
	    			print(f"Failed to decode email for {name}: {e}")

	    	if email == "Julie@GreenSourceDFW.org":
	    		email = None


	    	website = None
	    	website_container = soup_2.find("div", class_="field-name-field-url")
	    	if website_container:
	    		a_tag = website_container.find("a", href=True)
	    		if a_tag:
	    			website = a_tag["href"]

	    	phone_tag = soup_2.find("span", itemprop="telephone")
	    	phone = phone_tag.get_text().strip() if phone_tag else None

	    	if email:
	    		print(f"{name} has email: {email}")
	    	else:
	    		print(f"{name} has NO email")


	    	companies.append({
                "Company Name": name,
                "Link": company_url,
                "Location": location,
                "Email": email,
                "Website": website,
                "Phone": phone,
                "Business": business
            })

	next_btn = soup.find(class_ = "pager-next")
	url = next_btn.find("a")["href"] if next_btn else None


with open("green_businesses.csv", "w", newline="", encoding="utf-8") as file:
    headers = ["Company Name", "Link", "Location", "Email", "Website", "Phone", "Business"]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for company in companies:
        writer.writerow(company)

print("CSV file saved as green_businesses.csv")