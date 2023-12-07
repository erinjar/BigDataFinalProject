import pandas as pd
import matplotlib.pyplot as plt

# Load the merged CSV file
merged_df = pd.read_csv('merged_oscar_movies.csv')

# Specify the discrete rating values
discrete_ratings = [0.0, 1.0, 2.0, 3.0]

# Filter the dataframe to include only movies with "Winner" in the "Position" column
winner_df = merged_df[merged_df['Position'] == 'Winner']
filtered_df = winner_df[winner_df['rating'].isin(discrete_ratings)]

# Calculate the proportion of each score
proportions = filtered_df['rating'].value_counts(normalize=True, sort=False)

# Plotting a bar graph with text labels
plt.bar(proportions.index, proportions, color='skyblue', edgecolor='black')

# Add text labels above each bar
for rating, proportion in zip(proportions.index, proportions):
    plt.text(rating, proportion + 0.01, f'{proportion:.2%}', ha='center')

plt.xlabel('Bechdel Score')
plt.ylabel('Proportion')
plt.title('Proportion of Bechdel Scores for Oscar Best Picture Winners')
plt.show()