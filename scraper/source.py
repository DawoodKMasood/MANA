# Imports variables from "config.py" file
import config

# Return twitter API config as a variable
def twitter():
    # Initialize connection to MySQL database
    cursor = config.database.cursor()
    
    # Execute our database query
    cursor.execute("SELECT * FROM `twitter_source`")
    
    # Store results into `results` variable
    results = cursor.fetchall()
    
    # Reset DB cursor
    cursor.reset()
    
    # Return cursor
    return results

def news():
    # Initialize connection to MySQL database
    cursor = config.database.cursor()
    
    # Execute our database query
    cursor.execute("SELECT * FROM `news_source`")
    
    # Store results into `results` variable
    results = cursor.fetchall()
    
    # Reset DB cursor
    cursor.reset()
    
    # Return cursor
    return results