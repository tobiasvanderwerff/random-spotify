import spotipy
import spotipy.util as util
import random
import os

client_id       = os.environ['SPOTIPY_CLIENT_ID']
client_secret   = os.environ['SPOTIPY_CLIENT_SECRET']
username        = os.environ['SPOTIPY_USERNAME']
redirect_uri    = "http://localhost/"
scope           = "playlist-modify-private playlist-read-private streaming"

# Length of the random playlist that is generated.
playlist_len    = 100

token = util.prompt_for_user_token(username, scope, client_id=client_id,
        client_secret=client_secret, redirect_uri=redirect_uri)

if __name__ == "__main__":
    if token:
        sp = spotipy.Spotify(auth=token)

        print("Generating a random playlist of " + str(playlist_len) + 
              " tracks...")

        new_playlist = sp.user_playlist_create(username, "Random music",
                public=False, description=("Music randomly picked from all "
                                           "personal playlists"))
        all_playlists       = sp.user_playlists(username) 
        all_track_ids       = []
        for playlist in all_playlists['items']:
            tracks = sp.user_playlist(username, playlist['id'],
                    fields="tracks")
            for track in tracks['tracks']['items']:
                all_track_ids.append(track['track']['uri'])
        rand_sample = random.choices(all_track_ids, k=playlist_len)
        sp.user_playlist_add_tracks(username, new_playlist['id'], rand_sample)

        print("Done.")


        try:
            sp.start_playback(context_uri=new_playlist['uri'])
        except spotipy.client.SpotifyException: # No Spotify client reachable
            pass
    else:
        print("Unable to obtain authentication token")
