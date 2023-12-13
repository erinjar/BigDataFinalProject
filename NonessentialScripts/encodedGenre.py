import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

#Get Unique Genres
df = pd.read_csv('masterfile.csv') 
genres_list = df['genre'].str.split(', ').explode()
unique_genres = genres_list.unique()

print("Unique Genres:", unique_genres)
# Assuming 'genres' is a list of genres for each movie in your dataset
# Replace this with your actual genre data

# # Create a MultiLabelBinarizer instance
# mlb = MultiLabelBinarizer()

# # Fit and transform the genre data using one-hot encoding
# genre_encoded = mlb.fit_transform(unique_genres)
# print(genre_encoded)

# # Create a DataFrame with the one-hot encoded genre data
# genre_df = pd.DataFrame(genre_encoded, columns=mlb.classes_)

# Print the DataFrame
#print(genre_df)

