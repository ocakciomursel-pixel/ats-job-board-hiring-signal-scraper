"""
Greenhouse & Lever Company Job Board & Hiring Signal Scraper — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/ats-job-board-hiring-signal-scraper ($0.50 / 1,000 jobs)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~ats-job-board-hiring-signal-scraper/run-sync-get-dataset-items"

payload = {
    "companySlugs": [
        "stripe",
        "figma",
        "anthropic"
    ],
    "atsPlatform": "auto"
}

if __name__ == "__main__":
    print(f"Running Greenhouse & Lever Company Job Board & Hiring Signal Scraper on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
