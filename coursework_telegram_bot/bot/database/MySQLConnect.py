import pymysql
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

def create_connection():
    return pymysql.connect(
        host=os.getenv('host'),
        db=os.getenv('dbname'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        cursorclass=pymysql.cursors.DictCursor
    )


