import shodan

def main(args):
    domain = args.domain
    API_KEY = "vqvxEYCJo5zZBFQFHl6K96kW8RYfesXL"
    api = shodan.Shodan(API_KEY)

    query = f"hostname:{domain}"

    try:
        results = api.search(query)
        print(results)
        print(f"Results found: {results['total']}")
        for result in results['matches']:
            print(result)

    except shodan.APIError as e:
        print(f"Error : {e}")