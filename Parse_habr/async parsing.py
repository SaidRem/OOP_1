from bs4 import BeautifulSoup
from urllib.parse import urljoin
import asyncio
import aiohttp
import logging
import sys


DEBUG_MODE = False

logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.ERROR,
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


async def get_article_links(session, page_url):
    try:
        async with session.get(page_url, headers=headers) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), "lxml")
            soup_of_a = soup.select("article.tm-articles-list__item a.tm-title__link")
            article_links = [urljoin(BASE_URL, a.get("href")) for a in soup_of_a if a.get("href")]
            return article_links
    except (aiohttp.ClientError, asyncio.TimeoutError) as err:
        logging.debug(f"Failed to fetch article links from {page_url}: {err}")
        return []


async def fetch_html(session, url):
    try:
        async with session.get(url, headers=headers) as response:
            return await response.text()
    except (aiohttp.ConnectionError, asyncio.TimeoutError) as err:
        logging.debug(f"Failed to fetch {url}: {err}")
        return None


async def extract_article_data(session, url):
    html = await fetch_html(session, url)
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
        result = f'{art_date} - {title} - {url}'
    else:
        logging.debug(f'END extract_article_data: keywords didn\'t found in {url}')
        return None
    print(result)


async def main():
    async with aiohttp.ClientSession() as session:
        links = await get_article_links(session, ARTICLES_URL)
        tasks = [extract_article_data(session, url) for url in links]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
