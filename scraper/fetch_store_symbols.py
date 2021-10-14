# Imports `inspect` module
import inspect

# Imports `os` module
import os

# Imports `sys` module
import sys

# Get current directory path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Get parent directory from current directory path
parent_dir = os.path.dirname(current_dir)

# Insert `parent_dir` value into "SYS_PATH"
sys.path.insert(0, parent_dir)

# Imports variables from "config.py" file
import config

# Imports `Client` component from "binance" module
from binance.client import Client

# Imports Regex module
import re

# Imports `time` module for sleep
import time

def clean_symbol(symbol):
    # Replaces `USDT` with NULL leaving only base symbol
    result = symbol.replace("USDT", "")
    
    # Return `result`
    return result

def add_symbol_to_database(symbol, price):
    # Remove unneccessary symbol from the original symbol
    cleaned_symbol = clean_symbol(symbol)
    
    # Initialize connection to MySQL database
    cursor = config.database.cursor()
    
    # Query to insert symbol and price into `crypto` table
    symbol_insert_query = ("INSERT INTO `crypto` (symbol, price) VALUES (%s, %s)")
    
    # Query to update symbol with latest price if it already exists
    symbol_update_query = ("UPDATE `crypto` SET price = %s WHERE symbol = %s")
    
    # Execute our database query (Run query to check if symbol exists in database)
    cursor.execute(f"SELECT * FROM `crypto` WHERE symbol = '{cleaned_symbol}' LIMIT 1")
    
    # Fetch one record so we can apply if-condition
    result_exist = cursor.fetchone()
    
    if result_exist is None:
        try:
            # Execute our database query (Insert symbol and price into `crypto` table)
            cursor.execute(symbol_insert_query, (cleaned_symbol, price))
            
            # Make sure data is committed to the database
            config.database.commit()
            
            print(f"Symbol ({cleaned_symbol}) was added with price: {price}")
        except Exception as e:
            print(f"There was an error with inserting data: {e}")
    else:
        try:
            # Execute our database query (Update symbol with latest price if it already exists)
            cursor.execute(symbol_update_query, (cleaned_symbol, price))
            
            # Make sure data is committed to the database
            config.database.commit()
            
            print(f"Symbol ({cleaned_symbol}) was updated with price: {price}")
        except Exception as e:
            print(f"There was an error with updating data: {e}")
            
    # Reset DB cursor
    cursor.reset()

def fetch_binance_auth():
    # Initialize connection to MySQL database
    cursor = config.database.cursor()
    
    # Execute our database query
    cursor.execute("SELECT * FROM `api` WHERE RAND() AND (`api_key` IS NOT NULL AND `secret_key` IS NOT NULL) LIMIT 1")
    
    # Store results into `results` variable
    results = cursor.fetchone()
    
    # Reset DB cursor
    cursor.reset()
    
    # Return results
    return results

def commit():
    # Fetch Binance authentication (api_key & secret_key) from database
    binance_auth = fetch_binance_auth()
    
    # Initialize the Binance client with binance API key and Secret key
    client = Client(binance_auth[3], binance_auth[4])
    
    # Get exchange info from client
    exchange_info = client.get_exchange_info()
    
    # Sleeps for 200 miliseconds to avoid ban from API
    time.sleep(config.binance_api_limit)
    
    # Initialize an empty list of `symbols`
    symbols = []
    
    # Illiterate through the symbols we fetched from the client
    for s in exchange_info['symbols']:
        
        # Check if `base_symbol` from config matches
        if re.search(f'(?:{config.base_symbol})', str(s)):
            
            if str(s) != "USDTUSDT":
                # Fetches symbol current price
                p = client.get_symbol_ticker(symbol=s['symbol'])
                
                # Sleeps for 200 miliseconds to avoid ban from API
                time.sleep(config.binance_api_limit)
                
                # If it matches then append the string to `symbols` list
                add_symbol_to_database(s['symbol'], p['price'])