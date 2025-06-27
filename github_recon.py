import requests
import time

def search_github_repos_all(query, token, per_page=30, max_pages=10):
    all_repos = []
    urls_ext = ['code','repositories','issues','users','discussions','commits']
    print(query)
    for ext in urls_ext:
        url = f"https://api.github.com/search/{ext}"
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            headers["Authorization"] = f"token {token}"

        for page in range(1, max_pages + 1):
            # print(f"[+] Fetching page {page}")
            params = {
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": per_page,
                "page": page
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                repos = data.get("items", [])
                if not repos:
                    break  # No more results
                all_repos.extend(repos)
                time.sleep(1)  # Avoid rate limits
            else:
                print(f"[!] Error {response.status_code}: {response.text}")
                break

    return all_repos

def read_dorks_github(domain):
    queries = []
    with open('github_dorks.txt','r') as f:
        for line in f:
            q = domain + ' ' +  line.strip()
            queries.append(q)
    return queries

# Example usage
def main(args):
    token = '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'
    domain = args.domain
    queries = read_dorks_github(domain)
    for query in queries:
        results = search_github_repos_all(query, token, per_page=30, max_pages=5)
        for repo in results:
            print(f"{repo['html_url']}")
        