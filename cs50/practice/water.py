def main():
    moisture = int(sample())
    days = 1
    print(f"Day {days}: Moisture is {moisture}%")

    # repeats the question until moisture is below 20%
    while moisture > 20:
        moisture = int(sample())
        days +=1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")



def sample():
    return input("What percent moisture is the plant at? ")


main()
