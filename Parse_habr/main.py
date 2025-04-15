import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging


DEBUG_MODE = False

logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.CRITICAL,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
BASE_URL = 'https://habr.com'
ARTICLES_URL = urljoin(BASE_URL, '/ru/articles')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36"
}


def get_article_links(page_url):
    response = requests.get(page_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    article_links = []

    for a in soup.select("article.tm-articles-list__item a.tm-title__link"):
        href = a.get("href")
        if href:
            full_url = urljoin(BASE_URL, href)
            article_links.append(full_url)

    return article_links


def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_article_data(html, url):
    logging.debug(f'START extract_article_data for: {url}')
    soup = BeautifulSoup(html, 'lxml')

    # --- Title Extraction ---
    title_tag = soup.select_one('h1.tm-title.tm-title_h1 > span')
    logging.debug(f'SELECTOR h1.tm-title.tm-title_h1 => | {title_tag = }')
    if not title_tag:
        # Try to find title in <meta property="og:title">
        title_tag = soup.find('meta', attrs={'property': 'og:title'})
        logging.debug(f'<meta property="og:title"> => {title_tag = }')
        title = title_tag['content'] if title_tag else 'No_Title'
    else:
        title = title_tag.text.strip()

    # --- Date Extraction ---
    data_meta = (soup.find('meta', attrs={'property': 'article:published_time'})
                 or soup.find('meta', attrs={'property': 'aiturec:datetime'})
    )
    logging.debug(f'{data_meta = }')
    if data_meta:
        datetime_val = data_meta['content']
        art_date = datetime_val[:10]
    else:
        art_date = 'Unknown Date'

    # --- Content Text ---
    content_div = soup.select_one('div#post-content-body')

    if not content_div:
        logging.debug(f'END extract_article_data - content didn\'t found: {url}')
        return None

    content_text = content_div.get_text(separator=' ', strip=True).lower()

    # --- Keyword Matching ---
    if any(keyword.lower() in content_text for keyword in KEYWORDS):
        logging.debug(f'END extract_article_data: keywords found in {url}')
        return f'{art_date} - {title} - {url}'
    else:
        logging.debug(f'END extract_article_data: keywords didn\'t found in {url}')


def main(urls):
    for url in urls:
        try:
            html = fetch_html(url)
            result = extract_article_data(html, url)
            if result:
                print(result)
        except Exception as err:
            print(f'Error processing {url}: {err}')


if __name__ == '__main__':
    links = get_article_links(ARTICLES_URL)
    main(links)
