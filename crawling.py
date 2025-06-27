import requests
import argparse
import re
from urllib.parse import urljoin


visited = set()

def extract_urls(url, html):
    raw_links = re.findall(r'(?:href|src)=["\'](.*?)["\']', html, re.IGNORECASE)
    full_links = [urljoin(url, link) for link in raw_links]
    return full_links, re.findall(r'(?:href|src)=["\'](https?://[^"\']+)["\']', html, re.IGNORECASE)

def crawl(url, depth, domain):
    if url in visited or depth == 0:
        return
    print(f"{url}")
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return
        html = response.text
        full_links, urls = extract_urls(url, html)
        # domain = 'nasa.gov'
        for u in urls:
            if u not in visited and domain in u:
                crawl(u, depth - 1, domain)
        for j in full_links:
            if j not in visited and domain in j:
                crawl(j, depth - 1, domain)
    except Exception as e:
        print(f"Error visiting {url}: {e}")

# if __name__=="__main__":
#     args = getting_args()
#     domain = args.domain
#     start_url = 'https://' + domain
#     depth = 2 
#     if args.depth:
#         depth = int(args.depth)
#     crawl(start_url, depth)
    # print("\nAll visited URLs:")
    # for u in visited:
    #     print(f'{u}')