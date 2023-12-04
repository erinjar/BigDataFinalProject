import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with the 'bechdel' column
df = pd.read_csv('masterfile.csv')

# Plotting the distribution of Bechdel test scores
plt.figure(figsize=(8, 6))
df['bechdel'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Distribution of Bechdel Test Scores')
plt.xlabel('Bechdel Test Score')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()