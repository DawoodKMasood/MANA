# Imports `inspect` module
import inspect

# Imports `os` module
import os

# Imports `sys` module
import sys

# Imports `twitter_class.py` file
from twitter_class import *

# Imports `fetch_store_symbols` from crypto module
import fetch_store_symbols

# Imports `symbols.py` file
import symbols

# Get current directory path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Get parent directory from current directory path
parent_dir = os.path.dirname(current_dir)

# Insert `parent_dir` value into "SYS_PATH"
sys.path.insert(0, parent_dir)

# Imports variables from "config.py" file
import config

# Import `crypto_pairs` object from symbols
crypto_symbols = symbols.crypto_pairs()

def commit():
    # Initialize the `TwitterClient` class from 'twitter_class.py' file
    t = TwitterClient()
    
    for x in crypto_symbols:
        # Get tweets for every symbol stored in database
        tweets_list = t.get_tweets(x[1], 100)
        
        # Initialize connection to MySQL database
        cursor = config.database.cursor()
                
        for y in tweets_list:
            # Execute our database query (Run query to check if symbol exists in database)
            cursor.execute(f"SELECT * FROM `twitter_signals` WHERE status_id = '{y.id}' LIMIT 1")
            
            # Fetch one record so we can apply if-condition
            result_exist = cursor.fetchone()
            
            if result_exist is None:
                try:
                    # Query to insert symbol and price into `crypto` table
                    tweet_insert_query = ("INSERT INTO `twitter_signals` (username, symbol, tweet, status_id, date) VALUES (%s, %s, %s, %s, %s)")
                    
                    # Execute our database query (Insert username, symbol, tweet, date into `twitter_signals` table)
                    cursor.execute(tweet_insert_query, (y.user.screen_name, x[1], y.text, y.id_str, y.created_at))

                    # Make sure data is committed to the database
                    config.database.commit()
                    
                    print(f"Tweet from @({y.user.screen_name}) was added into database!")
                except e as Exception:
                    print("Error: " + e)
        
        # Reset DB cursor
        cursor.reset()