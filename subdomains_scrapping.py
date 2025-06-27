import requests
import time
import argparse


def crt_subs(url, domain, max_val):
    for attempt in range(1,max_val+1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                try:
                    data = response.json()
                    break
                except ValueError:
                    print("Error")
            else:
                # print(f"[!] Attempt {attempt}: Server returned status code {response.status_code}. Retrying...")
                continue
        except requests.exceptions.RequestException as e:
            # print(f"[!] Attempt {attempt}: Request failed: {e}. Retrying...")
            continue
        time.sleep(delay_seconds)

    subdomains = set()

    for i in data:
        name_value = i.get('name_value', '')
        for sub in name_value.split("\n"):
            if sub.endswith(f'.{domain}'):
                subdomains.add(sub.lstrip('*.').strip().lower())
        
    for sub in sorted(subdomains):
        print(sub)

def main(args):
    # domain = 'google.com'
    domain = args.domain
    url = 'https://crt.sh/json?q=' + domain

    max_val = 30
    delay_seconds = 3
    crt_subs(url, domain, max_val)
