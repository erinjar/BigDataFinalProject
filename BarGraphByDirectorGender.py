import csv
import matplotlib.pyplot as plt
from genderize import Genderize, GenderizeException
import time

csv_file_path = 'masterfile.csv'  # Update with your actual file path

def get_gender(name):
    # Use Genderize to predict the gender with error handling
    try:
        gender = Genderize().get(name)[0]['gender']
        return gender.lower()  # Convert to lowercase for consistency
    except GenderizeException as e:
        if 'Request limit too low' in str(e):
            # Handle rate limit exceeded, wait for reset time
            reset_time = int(e.headers.get('x-rate-limit-reset', 0))
            wait_time = max(0, reset_time - int(time.time()) + 5)  # Add a buffer time
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
            time.sleep(wait_time)
            return get_gender(name)  # Retry the request
        else:
            return 'unknown'

director_data = {'male': {'total': 0, 'score_3': 0}, 'female': {'total': 0, 'score_3': 0}, 'unknown': {'total': 0, 'score_3': 0}}

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        score = row.get('bechdel', '')
        director_name = row.get('director', '')  # Update with the actual column name

        # Predict the gender based on the director's name
        director_gender = get_gender(director_name)

        # Increment the total count for the director's gender
        director_data[director_gender]['total'] += 1

        # Increment the count for score 3 for the director's gender
        if score == '3':
            director_data[director_gender]['score_3'] += 1

# Calculate proportions
proportions = {gender: data['score_3'] / data['total'] if data['total'] > 0 else 0 for gender, data in director_data.items()}

# Create a bar plot
fig, ax = plt.subplots()
genders = list(proportions.keys())

proportion_values = [proportions[gender] for gender in genders]

ax.bar(genders, proportion_values, color=['skyblue', 'lightcoral', 'lightgray'])
ax.set_ylabel('Proportion of Movies with Score 3')
ax.set_title('Proportion of Movies with Score 3 by Director Gender')

plt.show()