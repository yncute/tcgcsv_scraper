import requests
import pandas as pd
import time
from src.config import (
    TCG_CATEGORIES, SCRAPE_URL_TEMPLATE, RATE_LIMIT_SECONDS,
    MAX_RETRIES, BACKOFF_FACTOR
)
from src.logger import get_logger

logger = get_logger("scraper")

def fetch_csv_with_retries(url):
    retries = 0
    backoff = 1
    while retries < MAX_RETRIES:
        try:
            logger.info(f"Fetching: {url}")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.content
        except Exception as e:
            logger.warning(f"Fetch failed ({retries+1}/{MAX_RETRIES}): {e}")
            time.sleep(backoff)
            backoff *= BACKOFF_FACTOR
            retries += 1
    logger.error(f"Failed to fetch {url} after {MAX_RETRIES} retries.")
    return None

def process_and_yield_batches(df, batch_size=500):
    for start in range(0, len(df), batch_size):
        yield df.iloc[start:start+batch_size].to_dict(orient="records")

def scrape_all():
    all_results = []
    for category in TCG_CATEGORIES:
        url = SCRAPE_URL_TEMPLATE.format(category=category.strip())
        csv_content = fetch_csv_with_retries(url)
        if not csv_content:
            continue
        try:
            df = pd.read_csv(pd.compat.StringIO(csv_content.decode('utf-8')))
            logger.info(f"Fetched {len(df)} records for {category}")
            for batch in process_and_yield_batches(df):
                all_results.append((category, batch))
        except Exception as e:
            logger.error(f"Error processing CSV for {category}: {e}")
        time.sleep(RATE_LIMIT_SECONDS)
    return all_results 