import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Load data
df = pd.read_csv('masterfile.csv')

# Drop rows with missing values
df = df.dropna(subset=['year', 'rating', 'gross(in $)', 'votes', 'genre', 'bechdel'])
df['year'] = pd.to_numeric(df['year'], errors='coerce').astype(int)

# Define the unique genres
unique_genres = ['Biography', 'Drama', 'Music', 'History', 'Romance', 'Comedy', 'Crime',
                 'Musical', 'Action', 'Thriller', 'Sport', 'Adventure', 'Family', 'War',
                 'Animation', 'Horror', 'Fantasy', 'Sci-Fi', 'Mystery', 'Western']

# Add columns for each unique genre
for genre in unique_genres:
    df[genre] = df['genre'].apply(lambda x: 1 if genre in x else 0)

# Drop the original 'genre' column if needed
#df = df.drop('genre', axis=1)

# Save the modified DataFrame back to CSV
df.to_csv('masterfile_with_encoded_genre.csv', index=False)