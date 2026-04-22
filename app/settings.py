import os
from dotenv import load_dotenv

load_dotenv()

# Database

DATABASE_URL = os.getenv("DATABASE_URL")

REFRESH_DB = True # avoid re-flushing data into the database
