# Spotify Song Analysis

This Streamlit application analyzes your top Spotify tracks and provides insights into various audio features such as danceability, energy, and valence.

## Features

- Fetches your top 10 Spotify tracks
- Displays audio features (danceability, energy, valence) of these tracks in a bar chart

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- A Spotify developer account

## Set up your Spotify developer account:

- Go to the Spotify Developer Dashboard.
- Log in and create a new application.
- Note down your Client ID and Client Secret.

## Install required libraries
- pandas
- spotipy
- streamlit
## Start a virtual environment and run main.py
- py -3 -m venv .my_project
- streamlit run main.py
## Code Explanation
- The script starts by importing the necessary libraries: spotipy, streamlit, pandas, and os.
- It retrieves Spotify API credentials from environment variables.
- It sets up the Spotify OAuth authentication and initializes a Spotify client.
- The app layout and components are created using Streamlit functions.
- The top 10 tracks and their audio features are fetched and displayed in a bar chart.
