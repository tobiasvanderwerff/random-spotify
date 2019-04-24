# spotify-random

A simple Python script which generates a Spotify playlist containing music
randomly selected from a users' existing playlists.

## Setup

1. Register app at https://developer.spotify.com/my-applications/
2. Edit your `~/.bashrc` to export the following values:
``bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_USERNAME='your-spotify-username'
``

## Installation

Install required packages:
``
pip install -r requirements.txt
``

Run the program: 
``
python3 main.py
``
