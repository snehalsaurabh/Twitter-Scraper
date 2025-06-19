# Twitter News Scraper

A Python script to scrape tweets from specified Twitter usernames using the ntscraper library.

## Features

- Scrapes tweets from multiple Twitter users
- Robust error handling with fallback Nitter instances
- Configurable number of tweets per user
- Rate limiting with delays between requests
- Comprehensive logging
- Saves results to CSV format

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Twitter-Scraper
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

Simply run the main script:
```bash
python scraper.py
```

The script will:
1. Scrape tweets from the predefined list of usernames
2. Save the results to `dataset_crime_2.csv`
3. Display progress and statistics in the console

### Customizing Configuration

Edit the `config.py` file to customize the scraping parameters:

```python
# List of Twitter usernames to scrape
USERNAMES = [
    'your_username_1',
    'your_username_2',
    # Add more usernames here
]

# Scraping parameters
TWEETS_PER_USER = 100
DELAY_BETWEEN_REQUESTS = 5  # seconds

# Output file
OUTPUT_FILE = "dataset_crime_2.csv"
```

### Advanced Configuration

You can also modify:
- **Nitter instances**: Update `NITTER_INSTANCES` list in `config.py` to use different Nitter servers
- **Logging level**: Change `LOG_LEVEL` to "DEBUG" for more detailed output
- **Output format**: Modify the `save_tweets_to_csv()` function for different output formats

## Output

The script generates a CSV file (`dataset_crime_2.csv`) containing the scraped tweets with all available metadata fields.

## Error Handling

The script includes robust error handling:
- Tries multiple Nitter instances if one fails
- Logs all operations and errors
- Continues processing even if some users fail
- Graceful handling of empty results

## Dependencies

- `ntscraper`: For scraping Twitter data via Nitter instances
- `pandas`: For data manipulation and CSV export
- `requests`: HTTP library (dependency of ntscraper)
- `beautifulsoup4`: HTML parsing (dependency of ntscraper)
- `lxml`: XML/HTML parser (dependency of ntscraper)

## Notes

- This scraper uses Nitter instances to access Twitter data
- Nitter instances may have varying availability
- The script includes delays to be respectful to the services
- Some Nitter instances may be temporarily unavailable

## Troubleshooting

If you encounter issues:

1. **ModuleNotFoundError**: Make sure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. **No tweets scraped**: Nitter instances may be down. The script tries multiple instances automatically.

3. **Rate limiting**: Increase the delay between requests if needed.

## Legal Notice

Please ensure you comply with Twitter's Terms of Service and applicable laws when scraping data. This tool is for educational and research purposes.