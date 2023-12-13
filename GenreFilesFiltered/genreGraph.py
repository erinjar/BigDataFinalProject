import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
genre = str(input("What Genre? ")) 
df = pd.read_csv('GenreFilesFiltered/' +genre + '_filtered.csv')

genre = genre.capitalize()

# Specify the column for which you want to create the bar graph
column_to_plot = 'bechdel'

# Count the occurrences of each value in the specified column
value_counts = df[column_to_plot].value_counts()

# Create a bar graph
plt.bar(value_counts.index, value_counts.values)

for i, value in enumerate(value_counts.values):
    plt.text(value_counts.index[i], value + 0.1, str(value), ha='center')

plt.title(f'Bar Graph of {str(genre)} Movie Bechdel Test Scores')
plt.xlabel('Bechdel Test Score')
plt.ylabel('Count')

# Set x-axis ticks to be the unique values in the column
plt.xticks(value_counts.index)

# Show the plot
plt.show()