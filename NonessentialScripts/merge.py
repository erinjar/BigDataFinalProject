import pandas as pd
import os

input_directory = 'GenreFilesFiltered/'

# Specify the output file where you want to save the merged data without duplicates
output_file = 'masterfile.csv'

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Loop through each CSV file in the specified directory
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Concatenate the current DataFrame with the merged DataFrame, removing duplicates
        merged_df = pd.concat([merged_df, df]).drop_duplicates()

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(output_file, index=False)