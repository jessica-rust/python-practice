"""
Project Name: Artwork
Purpose: Searches the Art Institute of Chicago API for artworks matching a query and returns a list of artwork titles
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
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


