import requests
import argparse
import re
from bs4 import BeautifulSoup


def google_dork_read(domain):
    l1 = []
    with open('google_dork_wordlist.txt','r') as f:
        for line in f:
            stripped = line.strip()
            if stripped and not re.search(r'(?<![-\w])site(?![-\w])',stripped):
                # if "site" not in line.strip():
                url = stripped + f' site:{domain}'
                # print(url)
                l1.append(url)
            # elif stripped and re.search(r'site(?![-\w])',line.strip()):
            #     print(stripped)
            else:
                url1 = re.sub(r'site:[^\s]+', '', stripped)
                url = url1 + f' site:{domain}'
                l1.append(url)
        return l1

def google_scarpping(domain, api_key, cx):
    list_of_dorks = google_dork_read(domain)
    for parameter_value in list_of_dorks:
        
        for start in range(1,100,10):
            # for using google as a scraper
            url = f'https://www.googleapis.com/customsearch/v1?q={parameter_value}&key={api_key}&cx={cx}&start={start}'
            # print(url)
            response = requests.get(url)
            results = response.json()
            # print(results)
            # print(f"Page number : {start}")
            if 'items' not in results:
                print(f"[INFO] No more results at start={start}")
                break
            for item in results["items"]:
                url1 = item["link"]
                print(url1)

                with open('results.txt','a') as file:
                    file.write(f'{url1}\n')
                    file.close()


def main(args):
    domain = args.domain
    api_key = 'AIzaSyC_Fn4QMbV_FRV9hgJnzdFKpLL1Qp9RHOY'
    cx = 'b02971f0e74214a3c'
    google_scarpping(domain, api_key, cx)