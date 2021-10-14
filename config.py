import mysql.connector

### EDIT VARIABLES BELOW THIS LINE ###

# The frequency with which the scraper will attempt to scrape content again. (DEFAULT: 3600)
scrape_freq = 3600

# Base Symbol that will be used to trade crypto coins with
base_symbol = "USDT"

# MySQL host to which our scraper will connect to.
mysql_host = "localhost"

# MySQL username and password with which our scraper will authenticate itself.
mysql_user = "root"
mysql_password = ""

# MySQL database to which our scraper will connect to.
mysql_database = "MANA"

### EDIT VARIABLES ABOVE THIS LINE ###

database = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# Binance API Limit for requests in seconds
binance_api_limit = 0.2
