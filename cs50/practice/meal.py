def main():
    input_time = input("What time is it? ")
    new_time =  convert(input_time)

    if 7 <= new_time <=8:
        print("breakfast time")
    elif 12 <= new_time <=13:
        print("lunch time")
    elif 18 <= new_time <=19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    minutes = float(minute)/60
    hours = float(hour)
    return hours + minutes

if __name__ == "__main__":
    main()
