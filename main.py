import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import pandas as pd

CLIENT_ID = '6082233ab1644e5483bfedce9c7850b3'
CLIENT_SECRET = 'd54efa4ad2dc486cb31d4b3a1dff0c56'
REDIRECT_URL = 'http://localhost:5000'

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = REDIRECT_URL,
        scope ='user-top-read'
    )
)

st.set_page_config(page_title='Spotify song analysis',page_icon='musical_note:')
st.title('Analysis for your top songs')
st.write('Discover insights abojut your spotify listening habits')

top_tracks = sp.current_user_top_tracks(limit = 10, time_range = 'short_term')
track_ids = [track['id'] for track in top_tracks['items']]
audio_features = sp.audio_features(track_ids)

df = pd.DataFrame(audio_features)
df['track_name'] = [track['name'] for track in top_tracks['items']]
df = df[['track_name','danceability','energy','valence']]
df.set_index('track_name',inplace=True)

st.subheader('Audio Feature for Top Tracks')
st.bar_chart(df,height=500)