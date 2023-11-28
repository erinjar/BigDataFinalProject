import csv
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = 'masterfile.csv'
output_csv_file_path = 'passage_by_year.csv'

# year_data = {}

# with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
#     csv_reader = csv.DictReader(csvfile)
    
#     for row in csv_reader:
#         year = row['year']
#         score = row['bechdel']

#         if year.isnumeric():
#             year = int(year)
        
#             # If the year is not already in the dictionary, add it
#             if year not in year_data:
#                 year_data[year] = {'0': 0, '1': 0, '2': 0, '3': 0, 'total': 0}
            
#             # Increment the count for the corresponding score
#             year_data[year][score] += 1
#             year_data[year]['total'] += 1

# # Print or use the data as needed
# for year, scores in year_data.items():
#     print(f'Year: {year}, Scores: {scores}')

# with open(output_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Year', 'Proportion_of_Score_3']
#     csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     csv_writer.writeheader()
    
#     for year, scores in year_data.items():
#         total_movies = scores.get('total', 0)
#         score_3_count = scores.get('3', 0)  # Fix here
        
#         proportion_score_3 = score_3_count / total_movies if total_movies > 0 else 0
#         csv_writer.writerow({'Year': year, 'Proportion_of_Score_3': proportion_score_3})

# Plotting the scatterplot
years = []
proportions = []

with open(output_csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        years.append(int(row['Year']))
        proportions.append(float(row['Proportion_of_Score_3']))

# Fit a linear regression line
coefficients = np.polyfit(years, proportions, 1)
polynomial = np.poly1d(coefficients)

plt.scatter(years, proportions, label='Proportion of Score 3')
plt.plot(years, polynomial(years), color='red', label='Line of Best Fit')
plt.xlabel('Year')
plt.ylabel('Proportion')
plt.title('Proportion of Movies that Pass Bechdel Test 2006-2023')
plt.legend()
plt.show()
