import pandas as pd

#print("This tool will filter one dataset by another, using the common columns.")

csv1 = "movies.csv"
input1 = str(input("What Genre? ")) 
csv2 = "MoviesByGenre/" + input1 + ".csv"



df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

c_csv1 = "imdbid"
c_csv2 = "movie_id"

filtered_df2 = df2[df2[c_csv2].isin(df1[c_csv1])]

output = input1 + "_filtered.csv"

filtered_df2.to_csv(output, index=False)

filtered_df3 = filtered_df2.copy()

filtered_df3.rename(columns={'movie_id': 'imdbid'}, inplace=True)

filtered_df3.to_csv(output, index=False)

# Read the original CSV file
file1 = pd.read_csv(output)

# Read the CSV file containing values for the new column
file2 = pd.read_csv('movies.csv')

# Merge the two dataframes based on a common column (e.g., 'common_column')
merged_df = pd.merge(file1, file2, on='imdbid')

# Add the new column to the original dataframe
file1['bechdel'] = merged_df['bechdel']

# Save the updated dataframe back to a CSV file
file1.to_csv(output, index=False)

