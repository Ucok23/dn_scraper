import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import logging
from requests.exceptions import RequestException


class DetikNewsScraper:
    def __init__(self):
        """Initialize the scraper with search URL and headers."""
        self.search_url = "https://www.detik.com/search/searchall?"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        logging.basicConfig(level=logging.INFO)

    def build_search_url(self, query: str, page_number: int) -> str:
        """Build search URL with query input and specific page number."""
        return f"{self.search_url}query={query}&siteid=3&sortby=time&sorttime=0&page={page_number}"

    def build_detail_url(self, url: str) -> str:
        """Build detail URL to turn off pagination in detail page."""
        a = urlsplit(url)
        return f"{a.scheme}://{a.netloc}{a.path}?single=1"

    def result_count(self, search_response: requests.Response) -> int:
        """Get search result count from the search response page."""
        soup = BeautifulSoup(search_response.text, "html.parser")
        tag = soup.find("span", "fl text")
        if tag:
            count = [int(s) for s in tag.text.split() if s.isdigit()]
            return count[0] if count else 0
        return 0

    def detail(self, url: str) -> str:
        """Get full article content from the given URL."""
        detail_url = self.build_detail_url(url)
        try:
            req = requests.get(detail_url, headers=self.headers)
            req.raise_for_status()
            soup = BeautifulSoup(req.text, "html.parser")
            return self._extract_body(soup)
        except RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
            return ""

    def get_article(self, url: str) -> str:
        """Get article content from the given URL."""
        try:
            req = requests.get(url, headers=self.headers)
            req.raise_for_status()
            soup = BeautifulSoup(req.text, "html.parser")
            return self._extract_body(soup)
        except RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
            return ""

    def _extract_body(self, soup: BeautifulSoup) -> str:
        """Extract article body from the BeautifulSoup object."""
        body = ""
        tag = soup.find("div", class_="detail__body-text") or soup.find("div", class_="itp_bodycontent")
        if tag:
            for p in tag.find_all("p"):
                body += p.text
        return body

    def parse(self, search_response: requests.Response, detail: bool = False, limit: int = None) -> list:
        """Parse the search response to extract article details."""
        soup = BeautifulSoup(search_response.text, "html.parser")
        articles = soup.find_all("article")
        data = []
        news_pattern = re.compile(r"https://news\.detik\.com/.*")
        count = 0

        for article in articles:
            if limit is not None and count >= limit:
                break

            judul = article.find("h3").find("a").text
            link = article.find("a").get("href")
            if not link or not news_pattern.match(link):
                continue
            gambar = article.find("img").get("src")
            body = self.detail(link) if detail else ""
            waktu = article.find("div", class_="media__date").find("span").get("title")
            data.append(
                {
                    "judul": judul,
                    "link": link,
                    "gambar": gambar,
                    "body": body,
                    "waktu": waktu,
                }
            )
            count += 1
        return data

    def search(self, query: str, page_number: int = 1, detail: bool = False, limit: int = None) -> list:
        """Search for articles based on the query and page number."""
        url = self.build_search_url(query, page_number)
        try:
            search_response = requests.get(url, headers=self.headers)
            search_response.raise_for_status()
            return self.parse(search_response, detail, limit)
        except RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
            return []
