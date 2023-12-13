import pandas as pd

df = pd.read_csv('masterfile_pronouns.csv')

def map_to_binary(value):
    if value == 3:
        return 1
    else:
        return 0


def map_sentiment(value):
    if value > 0.05:
        return 2
    elif -0.05 < value < 0.05:
        return 1
    elif value < -0.05:
        return 0

df['sentiment'] = df['sentiment'].apply(map_sentiment)
df['bechdel'] = df['bechdel'].apply(map_to_binary)

df.to_csv('modified_masterfile.csv', index=False)