import pandas as pd
from scipy.stats import pearsonr

# this shows very little correlation between any of the variables
# other than no. votes and rating, which is to be expected

df = pd.read_csv('masterfile_sentiment.csv')
df = df.dropna()

def calculate_correlation(col1, col2):
    try:
        correlation, _ = pearsonr(df[col1], df[col2])
        return correlation
    except ValueError:
        return None
    
columns = df.columns

for i in range(len(columns)):
    for j in range(i + 1, len(columns)):
        col1 = columns[i]
        col2 = columns[j]

        # Check if both columns are numeric
        if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
            correlation = calculate_correlation(col1, col2)

            if correlation is not None:
                print(f"Correlation between {col1} and {col2}: {correlation}")
            else:
                print(f"No correlation available for {col1} and {col2} (possibly due to missing values)")
        else:
            print(f"At least one of {col1} and {col2} is not numeric. Skipping correlation calculation.")
