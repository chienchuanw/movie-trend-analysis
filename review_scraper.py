import requests
from bs4 import BeautifulSoup
from typing import List


class IMDBScraper:
    def __init__(self, movie_id: str) -> None:
        self.movie_id = movie_id
        self.base_url = f"https://www.imdb.com/title/{movie_id}/reviews"

    def get_reviews(self) -> List[str]:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            )
        }
        session = requests.Session()
        response: requests.Response = session.get(self.base_url, headers=headers)
        response.raise_for_status()

        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        reviews = soup.find_all("div", class_="text show-more__control")

        return [review.get_text(strip=True) for review in reviews]


if __name__ == "__main__":
    movie_id: str = "tt22022452"
    scraper: IMDBScraper = IMDBScraper(movie_id)

    print(requests.get(scraper.base_url))

    # reviews: List[str] = scraper.get_reviews()
    # print(reviews)
