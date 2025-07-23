# TCG CSV Scraper

A production-ready Python scraper that fetches daily TCG product and price data from [tcgcsv.com](https://tcgcsv.com), uploads it to a Supabase database, and is fully automated via GitHub Actions.

## Features

- Daily automated scraping (configurable schedule)
- Batch processing for large datasets
- Retry logic with exponential backoff
- Comprehensive logging and error handling
- Database upsert functionality (no duplicates)
- Rate limiting to respect source website
- Manual workflow trigger support
- Supports multiple TCG categories (Pokemon, Magic, Yu-Gi-Oh, etc.)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/tcgcsv_scraper.git
cd tcgcsv_scraper
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and fill in your Supabase credentials.

### 4. Set up Supabase

- Create a new project at [Supabase](https://supabase.com/)
- Run the SQL in `sql/schema.sql` to create the required table.

### 5. Run locally

```bash
python src/main.py
```

### 6. Set up GitHub Actions

- Add your Supabase credentials as GitHub repository secrets:
  - `SUPABASE_URL`
  - `SUPABASE_KEY`
  - `SUPABASE_TABLE`
- The workflow runs daily and can be triggered manually.

## Security

- **Never commit your real `.env` file or secrets.**
- Use GitHub Secrets for all credentials.

## Monitoring

- All logs are output to the console and GitHub Actions logs.
- Add external monitoring/alerting as needed.

## License

MIT
