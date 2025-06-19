# Configuration file for Twitter News Scraper

# List of Twitter usernames to scrape
USERNAMES = [
    'alanhenney',
    'OCCRP', 
    'NOELreports',
    'CBSEveningNews',
    'CrimeChatt',
    'phivolcs_dost'
]

# Scraping parameters
TWEETS_PER_USER = 100
DELAY_BETWEEN_REQUESTS = 5  # seconds

# Output file
OUTPUT_FILE = "dataset_crime_2.csv"

# Nitter instances (fallback options) - Updated list with more reliable instances
NITTER_INSTANCES = [
    "https://nitter.privacydev.net",
    "https://nitter.unixfox.eu", 
    "https://nitter.1d4.us",
    "https://nitter.kavin.rocks",
    "https://nitter.fdn.fr",
    "https://nitter.42l.fr",
    "https://nitter.pussthecat.org"
]

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'