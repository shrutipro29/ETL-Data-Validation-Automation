import mysql.connector
from config.config import DB_CONFIG

def get_connection(database_name):
    connection = mysql.connector.connect(
        host = DB_CONFIG["host"],
        user = DB_CONFIG["user"],
        password = DB_CONFIG["password"],
        database=database_name
    )

    return connection