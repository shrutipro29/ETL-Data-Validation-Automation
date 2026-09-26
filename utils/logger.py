import logging
import os


# Create logs folder if it does not exist
os.makedirs("logs", exist_ok=True)


# Create our application logger
logger = logging.getLogger("etl_automation")

logger.setLevel(logging.INFO)

# Prevent messages from going to the root logger
logger.propagate = False


# File handler
file_handler = logging.FileHandler(
    "logs/etl_automation.log"
)

file_handler.setLevel(logging.INFO)


# Terminal handler
console_handler = logging.StreamHandler()

console_handler.setLevel(logging.INFO)


# Log format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Reduce MySQL Connector's logging
logging.getLogger("mysql.connector").setLevel(logging.WARNING)