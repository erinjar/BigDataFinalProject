import requests
import csv

def get_all_movie_ids():
    url = "http://bechdeltest.com/api/v1/getAllMovieIds"
    response = requests.get(url)
    data = response.json()
    return data

def write_to_csv(movie_ids, filename="movie_ids.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["imdbid", "id"])
        # Write data
        for movie_id in movie_ids:
            writer.writerow([movie_id["imdbid"], movie_id["id"]])

if __name__ == "__main__":
    movie_ids_data = get_all_movie_ids()
    write_to_csv(movie_ids_data)