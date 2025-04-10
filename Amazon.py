import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

all_data = []

for page in range(1, 21):
    print(f"Scraping page {page}...")
    url = f"https://www.amazon.in/s?k=camera&page={page}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    items = soup.find_all("div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16")

    for item in items:

        try:
            h2 = item.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
            title = h2.text.strip() if h2 else ""
        except:
            title = ""

        try:
            span_rating = item.find("span", class_="a-icon-alt")
            rating = span_rating.text.strip() if span_rating else ""
        except:
            rating = ""

        try:
            span_price = item.find("span", class_="a-price-whole")
            price = span_price.text.strip() if span_price else ""
        except:
            price = ""

        all_data.append({
            "title": title,
            "rating": rating,
            "price": price
        })

    time.sleep(2)  # Polite delay to avoid IP ban

# Write data to data.csv
import csv
with open("Amazon.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["title", "rating", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in all_data:
        writer.writerow(data)


