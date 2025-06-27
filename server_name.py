import requests

def name(args):
    domain = args.domain
    url = f'https://{domain}'
    response = requests.get(url)
    if response.headers['server']:
        print(f"[+] Server : {response.headers['server']}")