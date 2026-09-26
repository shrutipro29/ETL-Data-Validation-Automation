# DB_CONFIG = {
#     "host" : "localhost",
#     "user" : "root",
#     "password": "7982sP@#"
# }
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "source_database": os.getenv("SOURCE_DATABASE", "insurance_source"),
    "target_database": os.getenv("TARGET_DATABASE", "insurance_target")
}