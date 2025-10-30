# Required Libraries 📚
import re
import pandas as pd
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

# 🔑 Spotify API Authentication Setup
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='c67421da39774099a41ff239df0523ae',  # Replace with your Client ID
    client_secret='27afbcdee57c4c279dc3defbd48f74bf'  # Replace with your Client Secret
))

# 🛢️ MySQL Database Connection
db_config = {
    'host': 'localhost',       # Change to your MySQL host if needed
    'user': 'root',            # Replace with your MySQL username
    'password': 'Jump@123',    # Replace with your MySQL password
    'database': 'spotify_db'   # Replace with your database name
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# ✅ Ensure table exists
create_table_query = """
CREATE TABLE IF NOT EXISTS spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
)
"""
cursor.execute(create_table_query)
connection.commit()

# 📂 Read track URLs from file
file_path = "track_urls.txt"
with open(file_path, 'r') as file:
    track_urls = file.readlines()

# 🧠 Collect all track data
all_tracks = []

# 🔁 Process each URL
for track_url in track_urls:
    track_url = track_url.strip()  # Remove whitespace
    try:
        # Extract track ID from URL
        match = re.search(r'track/([a-zA-Z0-9]+)', track_url)
        if not match:
            print(f"Invalid URL format: {track_url}")
            continue

        track_id = match.group(1)

        # Fetch track details from Spotify API
        track = sp.track(track_id)

        # Extract metadata
        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': round(track['duration_ms'] / 60000, 2)
        }

        # Add to list
        all_tracks.append(track_data)

        # Insert data into MySQL
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))
        connection.commit()

        print(f"Inserted: {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")

# 🧾 Close MySQL connection
cursor.close()
connection.close()

# 📊 Save all track data to CSV
df = pd.DataFrame(all_tracks)
df.to_csv('spotify_track_data.csv', index=False)
print("✅ All tracks have been processed and saved to 'spotify_track_data.csv'.")

# 🎨 Visualization Example
if not df.empty:
    plt.figure(figsize=(8, 5))
    plt.bar(df['Track Name'], df['Popularity'], color='skyblue', edgecolor='black')
    plt.title("Track Popularity Comparison")
    plt.xlabel("Track Name")
    plt.ylabel("Popularity")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("No track data available for visualization.")
