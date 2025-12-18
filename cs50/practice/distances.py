distances = {
    "Voyager 1": 163,
    "voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main():
    # .keys() gives back a list of the dictionary's keys
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")
        print(distances.keys())
        
    # .values() gives back a list of the dictionary's values
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} meters")

def convert(au):
    return au * 149597870700


main()
