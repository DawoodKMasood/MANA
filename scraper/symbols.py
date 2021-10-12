# Imports variables from "config.py" file
import config

def crypto_pairs():
    # Initialize connection to MySQL database
    cursor = config.database.cursor()
    
    # Execute our database query
    cursor.execute("SELECT * FROM `crypto`")
    
    # Store results into `results` variable
    results = cursor.fetchall()
    
    # Reset DB cursor
    cursor.reset()
    
    # Return results
    return results