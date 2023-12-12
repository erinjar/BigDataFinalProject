import pandas as pd

# Load the first CSV with IMDb and rating columns
df1 = pd.read_csv('all_movies.csv')

# Load the second CSV with IMDb and other movie details
df2 = pd.read_csv('oscars.csv')

# Merge the two dataframes based on IMDb column
merged_df = pd.merge(df2, df1[['imdbid', 'rating']], on='imdbid', how='left')

# Save the merged dataframe to a new CSV
merged_df.to_csv('merged_oscar_movies.csv', index=False)