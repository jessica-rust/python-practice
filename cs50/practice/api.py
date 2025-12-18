import requests

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    # internet or connection can be lost so its best to have a check
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist} # this parameter was specified in the websites documentation
            )
        response.raise_for_status() # this raises the error
    except requests.HTTPError: # if connection cant be made this is the error that is raised
        print("Couldn't complete request!")
        return

    print(response) # prints the status of the request
    content = response.json() # converts the data received to json
    for artwork in content["data"]: # for each data key in json
        print(f"* {artwork["title"]}") # print the title key within


main()
