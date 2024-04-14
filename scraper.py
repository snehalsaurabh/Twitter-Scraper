from ntscraper import Nitter
import pandas as pd
import time  # Import time module for adding delays

# List of hashtags
#hashtags = ['news', 'burglary', 'terroristattack', 'fire', 'accident', 'war', 'riot', 'curfew', 'pandemic']
username = ['alanhenney','OCCRP','NOELreports','CBSEveningNews','CrimeChatt','phivolcs_dost']

# Initialize an empty list to store tweets
all_tweets = []

# Specify the Nitter instance
nitter_instance = "https://nitter.net"

# Iterate over hashtags
for hashtag in username:
    # Initialize Nitter scraper
    scraper = Nitter(log_level=1)

    # Get tweets for the current hashtag using the specified instance
    tweets = scraper.get_tweets(hashtag, mode="user", number=100, instance=nitter_instance)

    # Extend the list of all_tweets with tweets for the current hashtag
    all_tweets.extend(tweets['tweets'])

    # Add a delay before making the next request
    time.sleep(5)  # Add a delay of 5 seconds between requests

# Convert all_tweets list to a DataFrame
df = pd.DataFrame(all_tweets)

# Save DataFrame to CSV file
df.to_csv("dataset_crime_2.csv", index=False)
