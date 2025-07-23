from src.scraper import scrape_all
from src.supabase_client import upsert_products
from src.logger import get_logger

logger = get_logger("main")

def main():
    logger.info("Starting TCG CSV Scraper")
    results = scrape_all()
    for category, batch in results:
        try:
            upsert_products(batch)
        except Exception as e:
            logger.error(f"Failed to upsert batch for {category}: {e}")
    logger.info("Scraping complete.")

if __name__ == "__main__":
    main() 