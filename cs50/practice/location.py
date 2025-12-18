from sys import getsizeof
def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    latitude, longitude = coordinate_tuple # unpacking a tuple
    print(f"Latitude: {latitude}")
    print(f"Latitude: {longitude}")

    # using indexes
    print(f"Latitude: {coordinate_tuple[0]}")
    print(f"Latitude: {coordinate_tuple[1]}")

    # coordinate_tuple[0] = -42.376
    # this would give you an error bcause tuples cant be changed

    # size differences
    print(f"{getsizeof(coordinate_tuple)} bytes")
    print(f"{getsizeof(coordinate_list)} bytes")


main()
