import requests
import os
from dotenv import load_dotenv
from typing import Dict, List


class TMDBClient:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_popular_movie(self, page: int) -> List[Dict]:
        """
        獲取熱門電影的數據
        """

        url: str = f"{self.BASE_URL}/movie/popular?language=en-US&{page}=3"

        headers: Dict[str, str] = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_genre(self) -> List[Dict]:
        """
        獲取電影類型的數據
        """

        url: str = f"{self.BASE_URL}/genre/movie/list?language=en"

        headers: Dict[str, str] = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":

    load_dotenv()

    api_key: str = os.getenv("TMDB_API_ACCESS_TOKEN", "")
    if not api_key:
        raise ValueError(
            "Environment variable 'TMDB_API_ACCESS_TOKEN' is not set or empty"
        )
    client: TMDBClient = TMDBClient(api_key)

    popular_movies: List[Dict] = client.get_popular_movie(page=1)["results"]
    # print(f"popular movie: {popular_movies}")
    for movie in popular_movies:
        print(movie["original_title"])

    # genre: List[Dict] = client.get_genre()
    # print(f"genre: {genre}")
