
# Spotify Data Analytics

Analyzed Spotify dataset to explore trends in song popularity, genres, and artist performance using Python and visualization tools.
Cleaned and processed large datasets with Pandas and NumPy for accurate insights.
Identified key factors influencing track popularity through data visualization and exploratory analysis.



## Features

- Cleaned and preprocessed Spotify dataset to ensure data accuracy and consistency.

- Performed exploratory data analysis (EDA) to identify relationships between audio features and track popularity.

- Visualized insights using Matplotlib and Seaborn to highlight top artists genres, and music trends.

- Analyzed yearly trends to understand listener preferences and feature evolution  over time.

- Derived insights on how attributes like danceability, energy, and tempo
  influence song success.


## Installation

###  1. 🧩  Prerequisites

Before you begin, make sure you have:

Python 3.8+ installed

MySQL Server / MySQL Workbench installed and running

A Spotify Developer Account (for API credentials)


### 2. 🔑 Set Up Spotify API Credentials

Go to Spotify Developer Dashboard
.

Log in and create a new application.

Copy the Client ID and Client Secret.

### 3. 📚 Required Libraries

'''Python

import re

from spotipy.oauth2 import SpotifyClientCredentials

import spotipy

import mysql.connector

client_credentials_manager = SpotifyClientCredentials(
    
    client_id="YOUR_CLIENT_ID",
    
    client_secret="YOUR_CLIENT_SECRET"
)


'''

### 4. 🛢️ Python Connect to DataBase

import mysql.connector

db_config = {
    
    'host': 'your MySQL host',           
    'user': 'your username',       
    'password': 'your MySQL Password',   
    'database': 'your database name'      
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


### 5. 📊 Visualization Libraries

- import pandas as pd
- import numpy as np
- import matplotlib.pyplot as plt
- import seaborn as sns


    