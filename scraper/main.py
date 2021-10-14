# Imports `source.py` file
import source

# Import `news` object from source
news_source = source.news()

# Imports `fetch_store_symbols.py` file
import fetch_store_symbols

# Imports `fetch_store_tweets.py` file
import fetch_store_tweets

# This is the first function that will be called when this file is executed
def main():
    fetch_store_symbols.commit()
    #fetch_store_tweets.commit()

if __name__ == "__main__":
    main()