from ntscraper import Nitter
import pandas as pd
import time
import logging
from typing import List, Dict, Any
import config

# Configure logging
logging.basicConfig(level=getattr(logging, config.LOG_LEVEL), format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)

def scrape_twitter_users(usernames: List[str], tweets_per_user: int = 100, delay: int = 5) -> List[Dict[str, Any]]:
    """
    Scrape tweets from specified Twitter usernames.
    
    Args:
        usernames: List of Twitter usernames to scrape
        tweets_per_user: Number of tweets to fetch per user
        delay: Delay in seconds between requests
    
    Returns:
        List of tweet dictionaries
    """
    all_tweets = []
    
    # Use Nitter instances from config
    nitter_instances = config.NITTER_INSTANCES
    
    # Validate inputs
    if not usernames:
        logger.warning("No usernames provided for scraping")
        return all_tweets
    
    if tweets_per_user <= 0:
        logger.warning("tweets_per_user must be positive, using default value of 100")
        tweets_per_user = 100
    
    logger.info(f"Starting to scrape {len(usernames)} users, {tweets_per_user} tweets per user")
    
    for i, username in enumerate(usernames, 1):
        logger.info(f"[{i}/{len(usernames)}] Scraping tweets from user: {username}")
        
        # Clean username (remove @ if present)
        username = username.lstrip('@')
        
        # Try different instances if one fails
        success = False
        for instance_idx, instance in enumerate(nitter_instances, 1):
            try:
                logger.debug(f"Trying instance {instance_idx}/{len(nitter_instances)}: {instance}")
                
                # Initialize Nitter scraper
                scraper = Nitter(log_level=1, skip_instance_check=False)
                
                # Get tweets for the current user
                tweets = scraper.get_tweets(username, mode="user", number=tweets_per_user, instance=instance)
                
                if tweets and 'tweets' in tweets and tweets['tweets']:
                    # Add username to each tweet for tracking
                    for tweet in tweets['tweets']:
                        tweet['scraped_username'] = username
                    
                    all_tweets.extend(tweets['tweets'])
                    logger.info(f"Successfully scraped {len(tweets['tweets'])} tweets from {username} using {instance}")
                    success = True
                    break
                else:
                    logger.warning(f"No tweets found for {username} using {instance}")
                    
            except Exception as e:
                logger.error(f"Error scraping {username} with {instance}: {str(e)}")
                # Add a small delay before trying next instance
                time.sleep(1)
                continue
        
        if not success:
            logger.error(f"Failed to scrape tweets from {username} with all {len(nitter_instances)} instances")
        
        # Add delay between requests to be respectful
        if i < len(usernames):  # Don't delay after the last user
            logger.debug(f"Waiting {delay} seconds before next user...")
            time.sleep(delay)
    
    return all_tweets

def save_tweets_to_csv(tweets: List[Dict[str, Any]], output_file: str) -> bool:
    """
    Save tweets to CSV file with error handling.
    
    Args:
        tweets: List of tweet dictionaries
        output_file: Path to output CSV file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        if not tweets:
            logger.warning("No tweets to save")
            return False
            
        # Convert to DataFrame
        df = pd.DataFrame(tweets)
        
        # Save to CSV
        df.to_csv(output_file, index=False)
        
        logger.info(f"Successfully saved {len(tweets)} tweets to {output_file}")
        logger.info(f"DataFrame shape: {df.shape}")
        logger.info(f"Columns: {list(df.columns)}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error saving tweets to CSV: {str(e)}")
        return False

def main():
    """Main function to execute the scraping process."""
    try:
        logger.info("Starting Twitter scraping process...")
        logger.info(f"Target usernames: {config.USERNAMES}")
        logger.info(f"Tweets per user: {config.TWEETS_PER_USER}")
        logger.info(f"Delay between requests: {config.DELAY_BETWEEN_REQUESTS} seconds")
        
        # Scrape tweets using configuration
        all_tweets = scrape_twitter_users(
            config.USERNAMES, 
            tweets_per_user=config.TWEETS_PER_USER, 
            delay=config.DELAY_BETWEEN_REQUESTS
        )
        
        if all_tweets:
            # Save tweets to CSV
            success = save_tweets_to_csv(all_tweets, config.OUTPUT_FILE)
            if success:
                logger.info("Scraping process completed successfully!")
            else:
                logger.error("Failed to save tweets to file")
        else:
            logger.warning("No tweets were scraped successfully")
            logger.info("This could be due to:")
            logger.info("- Nitter instances being unavailable")
            logger.info("- User accounts being private or non-existent")
            logger.info("- Rate limiting or network issues")
            
    except KeyboardInterrupt:
        logger.info("Scraping process interrupted by user")
    except Exception as e:
        logger.error(f"An error occurred during the scraping process: {str(e)}")
        logger.error("Please check your internet connection and try again")

if __name__ == "__main__":
    main()