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