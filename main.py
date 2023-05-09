import sqlalchemy
import pandas as pd
import timestamp as timestamp
from pandas import DataFrame
from sqlalchemy.orm import sessionmaker
import requests
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_track.sqlite"
USER_ID = "lifewithkarcia"
TOKEN = "BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11"

if __name__ == "main":
    headers = {
        "Accept": "Application/json",
        "Content-Type": "Application/json",
        "Authorization": "Bearer{token}".format(token=TOKEN)

    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    r = requests.get(
        "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp),
        header=headers)
    data = r.json()
    song_name = []
    artist_names = []
    played_at_list = []
    timestamp = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamp.append(song["played_at"][0:10])

        song_dict = {
            "song_names": song_names,
            "artist_name": artist_names,
            "played_at": played_at_list,
            "timestamp": timestamps
        }
        song_df: DataFrame = pd.DataFrame(song_dict, columns=["song_name", "artist_names", "played_at_list", "timestamp"])
print(song_df)
