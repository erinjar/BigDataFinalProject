# this is only useful if the movie's description isnt in a file,
# since you get rate limited by imdb fairly quickly

from imdb import IMDb
#from nltk import download
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def plot_sentiment_analysis(movie_id):
    #Download NLTK stopwords and punkt
    #download('stopwords')   #comment these out after running the test.py as 
    #download('punkt')       #the check to see if they're installed takes forever
    stop_words = set(stopwords.words('english'))

    ia = IMDb()
    movie = ia.get_movie(movie_id)
    description = movie.get('plot')[0]

    #Tokenize description
    words = word_tokenize(description)

    # Filter out stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join filtered words into a string
    filtered_description = ' '.join(filtered_words)

    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(filtered_description)['compound']

    return sentiment_score