import pandas as pd
#from nltk import download
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv('masterfile.csv')

def plot_sentiment_analysis(description):
    #Download NLTK stopwords and punkt
    #download('stopwords')   #comment these out after running the test.py as 
    #download('punkt')       #the check to see if they're installed takes forever
    stop_words = set(stopwords.words('english'))

    #Tokenize description
    words = word_tokenize(description)

    # Filter out stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join filtered words into a string
    filtered_description = ' '.join(filtered_words)

    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(filtered_description)['compound']

    return sentiment_score


def analyze_sentiment(description):
    sentiment_result = plot_sentiment_analysis(description)
    return sentiment_result

df['sentiment'] = df['description'].apply(analyze_sentiment)

df.to_csv('masterfile_sentiment.csv', index=False)