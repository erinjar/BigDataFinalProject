import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('all_movies.csv')

# Specify the column you want to modify
column_name = 'imdbid'

# Add "tt" to the beginning of each item in the specified column
df[column_name] = 'tt' + df[column_name].astype(str).str[:-2]

# Save the modified DataFrame back to a CSV file
df.to_csv('movies.csv', index=False)