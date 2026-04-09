from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from urllib.error import URLError, HTTPError
from urllib.request import ProxyHandler, Request, build_opener


class H2HeadlineParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h2 = False
        self.current_parts = []
        self.headlines = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'h2':
            self.in_h2 = True
            self.current_parts = []

    def handle_data(self, data):
        if self.in_h2:
            self.current_parts.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == 'h2' and self.in_h2:
            headline = ''.join(self.current_parts).strip()
            if headline:
                self.headlines.append(headline)
            self.in_h2 = False
            self.current_parts = []


def scrape_headlines(url):
    try:
        opener = build_opener(ProxyHandler({}))
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with opener.open(request, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')

        parser = H2HeadlineParser()
        parser.feed(html)
        return (url, parser.headlines)
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        print(f"Error occurred while scraping {url}: {error}")
        return (url, [])


if __name__ == '__main__':
    urls = [
        'https://www.bbc.com/news',
        'https://www.cnn.com',
        'https://www.nytimes.com',
        'https://www.theguardian.com/international',
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(scrape_headlines, urls))

    for url, headlines in results:
        print(f"\n--- Headlines from {url} ---")
        for headline in headlines[:10]:
            print(headline)
