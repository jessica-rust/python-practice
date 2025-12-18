import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=4aba7eccd1ef1cb0581ddb71968246ac941563d55e4b28987cc88b4c658ed68e")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    calc_price = n * price
    print(f"${calc_price:,.4f}")


main()
