import os
import csv
import matplotlib.pyplot as plt
import numpy as np

folder_path = 'GenreFilesFiltered'  # Update with your actual folder path

genre_data = {}

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Assuming each file is a CSV with a column titled 'bechdel'
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            score = row.get('bechdel', '')

            # If the genre (filename) is not already in the dictionary, add it
            if filename not in genre_data:
                genre_data[filename] = {'total': 0, 'score_3': 0}
            
            # Increment the total count and the count for score 3
            genre_data[filename]['total'] += 1
            if score == '3':
                genre_data[filename]['score_3'] += 1

# Calculate proportions
proportions = {genre: data['score_3'] / data['total'] if data['total'] > 0 else 0 for genre, data in genre_data.items()}

# Sort genres by proportion (from lowest to highest)
sorted_genres = sorted(proportions.keys(), key=lambda x: proportions[x])

# Create a bar plot
fig, ax = plt.subplots()
genres = list(sorted_genres)
labels = [genre.split('_filtered.csv')[0] for genre in genres]  # Use the abbreviation or the first 3 characters

proportion_values = [proportions[genre] for genre in genres]

# Store the bars to use in the text annotations
bars = ax.barh(labels, proportion_values, color='skyblue')
ax.set_xlabel('Proportion That Pass')
ax.set_title('Proportion of Movies that Pass Bechdel Test By Genre')

# Add proportion annotations at the end of each bar
for bar, proportion in zip(bars, proportion_values):
    ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2, f'{proportion:.2%}', va='center')

plt.show()
