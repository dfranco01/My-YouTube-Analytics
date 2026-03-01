#import pandas as pd
#from googleapiclient.discovery import build
#from dotenv import load_dotenv, find_dotenv
#import os

#env_path = find_dotenv()
#load_dotenv(env_path)

#API_KEY = os.getenv("API_KEY")

#print("Step off")
#api_service_name = "youtube"
#api_version = "v3"

# Get credentials and create an API client
#youtube = build(
#    api_service_name, api_version, developerKey=API_KEY)

#request = youtube.channels().list(
#    part="snippet,contentDetails,statistics",
#    id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
#)
#response = request.execute()
#pprint(response)
#print(response)
