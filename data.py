from data_literal import data
import pandas as pd
import sqlite3
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_KEY = os.getenv("API_KEY")

youtube = build('youtube', 'v3', developerKey=API_KEY)

request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

print(response)