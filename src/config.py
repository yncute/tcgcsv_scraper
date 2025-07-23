import os
from dotenv import load_dotenv

load_dotenv()

TCG_CATEGORIES = os.getenv("TCG_CATEGORIES", "pokemon,magic,yugioh").split(",")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_TABLE = os.getenv("SUPABASE_TABLE", "tcg_products")
SCRAPE_URL_TEMPLATE = os.getenv("SCRAPE_URL_TEMPLATE", "https://tcgcsv.com/{category}/ProductsAndPrices.csv")
RATE_LIMIT_SECONDS = int(os.getenv("RATE_LIMIT_SECONDS", "5"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "5"))
BACKOFF_FACTOR = float(os.getenv("BACKOFF_FACTOR", "2.0")) 