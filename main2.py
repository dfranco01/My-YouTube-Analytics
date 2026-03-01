import sqlite3
import pandas as pd

with sqlite3.connect('data.db') as connection:
    df = pd.read_sql_query("select * from YouTubeTable;", connection)
print("Opened db successfully")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())