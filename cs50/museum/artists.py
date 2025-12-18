"""
Project Name: Artists
Purpose: Searches the Art Institute of Chicago API for artists matching a query and returns a list of artist names
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
import requests

# searches for artists in the database with names similar to whats entered
def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit} # this parameter was specified in the websites documentation
            )
        response.raise_for_status() # this raises the error
    except requests.HTTPError: # if connection cant be made this is the error that is raised
        print("Couldn't complete request!")
        return []

    content = response.json()
    return [artist["title"] for artist in content["data"]]
