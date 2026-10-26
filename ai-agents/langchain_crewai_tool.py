"""
Greenhouse & Lever Company Job Board & Hiring Signal Scraper — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/ats-job-board-hiring-signal-scraper ($0.50 / 1,000 jobs)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~ats-job-board-hiring-signal-scraper/run-sync-get-dataset-items"

def run_ats_job_board_hiring_signal_scraper(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes Greenhouse & Lever Company Job Board & Hiring Signal Scraper on Apify Cloud ($0.50/1k jobs).
    Scrape active job openings, department growth breakdowns, remote/hybrid flags, tech stack requirements, and B2B buying intent signals directly from Greenhouse and Lever ATS company boards.
    """
    default_payload = {
    "companySlugs": [
        "stripe",
        "figma",
        "anthropic"
    ],
    "atsPlatform": "auto"
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
