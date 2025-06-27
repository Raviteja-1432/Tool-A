import crawling 
import dns_enum
import google_dorking
import subdomains_scrapping
import argparse
import shodan_search
import github_recon
import server_name

def getting_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help='Target domain', required=True)
    parser.add_argument('-k','--keyword', help='Keyword to search for google dorking', required=False)
    
    return parser.parse_args()

args = getting_args()
domain = args.domain
start_url = 'https://' + domain
depth = 4
print("Result of DNS Records")
print("---------------------------------------------------------------------------------------")
dns_enum.main(args)
print()
print("Result of subdomain scrapping")
print("---------------------------------------------------------------------------------------")
subdomains_scrapping.main(args)
print()
print("Result of Crawling Urls")
print("---------------------------------------------------------------------------------------")
crawling.crawl(start_url, depth, domain)
print()
print("Result of Google dorking urls")
print("---------------------------------------------------------------------------------------")
google_dorking.main(args)
print()
print("Result of shodan search")
print("---------------------------------------------------------------------------------------")
shodan_search.main(args)
print()
print("Result of github search")
print("---------------------------------------------------------------------------------------")
github_recon.main(args)
print()
print("Result of Server name")
print("---------------------------------------------------------------------------------------")
server_name.name(args)
print()