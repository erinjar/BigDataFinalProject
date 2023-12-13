import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('masterfile_sentiment.csv')

sns.set(style="whitegrid")

# Plotting
plt.figure(figsize=(10, 6))


def map_to_binary(value):
    if value == 3:
        return 1
    else:
        return 0

df['bechdel'] = df['bechdel'].apply(map_to_binary)

print(f"The covariance is {np.cov(df['bechdel'], df['sentiment'])}")
print(f"The correlcation is {np.corrcoef(df['bechdel'], df['sentiment'])}")
