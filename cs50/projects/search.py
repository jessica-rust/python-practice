"""
Project Name: Art Institute Search
Purpose: Searches for artists and artworks using custom modules and displays the top results
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
# museum is the package, artwork is the module, get_artworks is the function
from museum.artwork import get_artworks
from museum.artists import get_artists

def main():
    artist = input("Artist: ") # searches for artists
    artists = get_artists(query=artist, limit = 3)
    for artist in artists:
        print(f"* {artist}")
    artwork = input("Artwork: ") # searches for artworks
    artworks = get_artworks(query=artwork, limit = 3)
    for artwork in artworks:
        print(f"* {artwork}")



main()


