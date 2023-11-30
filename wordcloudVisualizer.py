import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

df = pd.read_csv('masterfile_sentiment.csv')

# concatenates all descriptions into a single string
text = ' '.join(df['description'].astype(str))

# tokenizes text
tokens = word_tokenize(text)

# remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

# calculate frequencies
word_freq = Counter(filtered_tokens)

# most common words
print("Most Prominent Words:")
for word, freq in word_freq.most_common(10):
    print(f"{word}: {freq} times")

# least common words
print("\nLeast Prominent Words:")
for word, freq in word_freq.most_common()[:-11:-1]:
    print(f"{word}: {freq} times")

# generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# predefining bins
bins = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700]

# count words falling into each bucket
bin_counts = {f'{start}-{end}': sum(1 for freq in word_freq.values() if start <= freq <= end) for start, end in zip(bins, bins[1:])}

# display the bucket counts
print("\nBucket Counts:")
for bucket, count in bin_counts.items():
    print(f"{bucket}: {count} words")

# create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# plot word cloud
ax1.imshow(wordcloud, interpolation='bilinear')
ax1.axis('off')
ax1.set_title('Word Cloud')

# plot the histogram of word frequencies
ax2.bar(bin_counts.keys(), bin_counts.values(), color='skyblue')
ax2.set_title('Word Frequency Distribution')
ax2.set_xlabel('Frequency')
ax2.set_yscale('log')
ax2.tick_params(axis='x', rotation=45, labelsize=6)  # Corrected line
ax2.set_ylabel('Number of Words')

plt.tight_layout()
plt.show()