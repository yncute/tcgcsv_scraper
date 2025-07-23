from supabase import create_client, Client
from src.config import SUPABASE_URL, SUPABASE_KEY, SUPABASE_TABLE
from src.logger import get_logger

logger = get_logger("supabase")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def upsert_products(data):
    supabase = get_supabase_client()
    try:
        response = supabase.table(SUPABASE_TABLE).upsert(data).execute()
        logger.info(f"Upserted {len(data)} records to Supabase.")
        return response
    except Exception as e:
        logger.error(f"Supabase upsert failed: {e}")
        raise 