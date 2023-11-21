import requests
import csv

def get_all_movies():
    api_url = "http://bechdeltest.com/api/v1/getAllMovies"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def create_csv(data, csv_filename):
    if data:
        fields = ["id", "imdbid", "title", "year", "rating"]
        
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
            
            csvwriter.writeheader()
            
            for movie in data:
                csvwriter.writerow(movie)

if __name__ == "__main__":
    all_movies = get_all_movies()
    
    if all_movies:
        create_csv(all_movies, "all_movies.csv")
        print("CSV file created successfully.")
    else:
        print("Failed to retrieve data from the API.")