import requests
import argparse


def dnsenumeration_A(data):
    # print(data)
    data = data
    print()
    print("A Records:")
    print("---------------------------------------------------------------------------------------")
    for i in data.get('a', []):
        host = i.get('host')
        if host:
            for entry in i.get('ips',[]):
                ip = entry.get('ip')
                banners = entry.get('banners', {})
                banner_list = []
                for service, details in banners.items():
                    if isinstance(details, dict):
                        banner_text = details.get('banner') or details.get('server')
                        if banner_text:
                            banner_list.append(f"{service.upper()}: {banner_text.strip()}")

                banner_output = " | ".join(banner_list) if banner_list else "No banner"
                print(f"{host.ljust(30)} {ip.ljust(18)} {banner_output}")

def dnsenumeration_MX(data):
    print("\n")
    print("MX Records")
    print("---------------------------------------------------------------------------------------")
    for i in data.get('mx', []):
        host = i.get('host')
        if host:
            for entry in i.get('ips', []):
                ip = entry.get('ip')
                if ip:
                    print(f"{host.ljust(30)} {ip.ljust(18)}")

def dnsenumeration_NS(data):
    print("\n")
    print("NS Records")
    print("---------------------------------------------------------------------------------------")
    for i in data.get('ns', []):
        host = i.get('host')
        if host:
            for entry in i.get('ips', []):
                ip = entry.get('ip')
                if ip:
                    print(f"{host.ljust(30)} {ip.ljust(18)}")

def dnsenumeration_TXT(data):
    print("\n")
    print("TXT Records")
    print("---------------------------------------------------------------------------------------")
    for i in data.get('txt', []):
        print(i)

def main(args):
    # args = getting_args()
    domain = args.domain
    headers = {
        "X-API-KEY": "423d21ac694f5a0f899a64e28b400199457b62553c89892a81a69286c5bc87de"
    }
    url = f'https://api.dnsdumpster.com/domain/{domain}'

    response = requests.get(url, headers=headers)
    # response2json = response.text
    data = response.json()
    dnsenumeration_A(data)
    dnsenumeration_MX(data)
    dnsenumeration_NS(data)
    dnsenumeration_TXT(data)