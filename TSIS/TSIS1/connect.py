import psycopg2
from config import DB_CONFIG

def get_connection():
    con = psycopg2.connect(**DB_CONFIG)
    return con
