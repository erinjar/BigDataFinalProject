import pandas as pd
from sentimentAnalysis import plot_sentiment_analysis

df = pd.read_csv('masterfile.csv')

df['imdb_id'] = df['imdbid'].apply(lambda x: x[2:])

def analyze_sentiment(imdb_id):
    sentiment_result = plot_sentiment_analysis(imdb_id)
    return sentiment_result

df['sentiment'] = df['imdb_id'].apply(analyze_sentiment)

df.to_csv('masterfile_sentiment.csv', index=False)