from bs4 import BeautifulSoup
import requests

spotify_client_id = "0ddb9ed864a0482bbb8727adfe50fc59"
spotify_client_secret = "59993b6df4c34eceb75ecb68105dc56e"
redirect = "http://example.com"

date = input("Enter a date in YYYY-MM-DD format: ")
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url = url)
content = response.text
soup = BeautifulSoup(content, "html.parser")
all_songtitles = soup.find_all("span", class_ = "chart-element__information__song text--truncate color--primary")
Song_titles = [song.getText() for song in all_songtitles]
print(Song_titles)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= "0ddb9ed864a0482bbb8727adfe50fc59",
        client_secret= "59993b6df4c34eceb75ecb68105dc56e",
        show_dialog=True,
        cache_path="./p46-SpotifyPlaylist/token.txt"
    )
)

user_id = sp.current_user()["id"]
song_uris = []
for song in Song_titles:
    year = date.split("-")[0]
    q = f"track: {song} year: {year}"
    result = sp.search(q = q, type= "track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
name = f"{date} Top Songs"
playlist = sp.user_playlist_create(user= user_id, name= name, public = False)

sp.playlist_add_items(playlist_id= playlist['id'], items= song_uris)
