import requests

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit} # this parameter was specified in the websites documentation
            )
        response.raise_for_status() # this raises the error
    except requests.HTTPError: # if connection cant be made this is the error that is raised
        print("Couldn't complete request!")
        return []

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]


