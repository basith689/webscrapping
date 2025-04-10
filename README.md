📸 Amazon Camera Scraper
This Python script scrapes camera product data from the Amazon India website. It extracts the title, rating, and price for the first 20 pages of search results and stores the information in a CSV file (Amazon.csv).

🚀 Features
Scrapes camera listings from https://www.amazon.in

Extracts:

Product Title

Rating

Price

Handles missing data gracefully

Polite delay between page requests to avoid IP bans

Outputs data to a CSV file for easy analysis

🛠 Requirements
Python 3.x

requests

beautifulsoup4

Install the required packages using:
pip install requests beautifulsoup4


📂 Usage
Clone this repository or download the Amazon.py script.

Run the script:
python Amazon.py


After execution, a file named Amazon.csv will be created in your directory with the scraped data.

⚠️ Notes
This script is for educational purposes only.

Web scraping may violate Amazon’s terms of service. Use responsibly.

The HTML structure of Amazon pages may change, so the script might need updates if it stops working.

🧠 Author
Bajithu R
