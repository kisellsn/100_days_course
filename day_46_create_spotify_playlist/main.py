import os

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

SONG_BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100"

# date = input("What year do you want to travel to? Type the date in the format: YYYY-MM-DD")
date = "2004-01-03"
response = requests.get(f"{SONG_BILLBOARD_ENDPOINT}/{date}")
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

REDIRECT_URI = os.getenv("REDIRECT_URI")
USERNAME = os.getenv("USERNAME")
scope = "user-library-read playlist-modify-public playlist-modify-private"

auth_manager = SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                            redirect_uri=REDIRECT_URI,
                            show_dialog=True,
                            cache_path="token.txt",
                            username=USERNAME,
                            scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]

song_uris = []

for song in song_names:
    try:
        uri = sp.search(q=f"track: {song} year: {date.split('-')[0]}",
                  type="track", limit=1)["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(user_id, f"{date.split('-')[0]} vibes", public=True)["id"]
sp.playlist_add_items(playlist_id, song_uris)