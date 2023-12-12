import requests
import pandas as pd

base_url = "http://bechdeltest.com/api/v1/"

def get_movie_by_imdb_id(imdb_id):
    url = f"{base_url}getMovieByImdbId?imdbid={imdb_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_info = response.json()
        print("Movie Information:")
        print(f"Title: {movie_info['title']}")
        print(f"Rating: {movie_info['rating']}")
    else:
        print(f"Error: {response.status_code} - {response.json()['description']}")

def get_movies_by_title(title):
    url = f"{base_url}getMoviesByTitle?title={title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        movies = response.json()
        for movie in movies:
            if(movie['title'] == title):
                print(f"Title: {movie['title']}, Rating: {movie['rating']}")
    else:
        print(f"Error: {response.status_code} - {response.json()['description']}")



# Example use
# legally_blonde_id = "0250494"
#get_movie_by_imdb_id("0111161")
#get_movies_by_title("Titanic")

df = pd.read_csv('masterfile.csv')

# Clean the 'year' column and convert to integer
df['year'] = pd.to_numeric(df['year'], errors='coerce').fillna(0).astype(int)

# Get the number of rows in the DataFrame
num_rows = df.shape[0]

print(f'The CSV file has {num_rows} rows.')