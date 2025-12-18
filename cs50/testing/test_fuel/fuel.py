def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
    except ValueError:
        # Non-integer input
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0:
        raise ValueError

    percent = round((x / y) * 100)
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


# old code
# def main():
#     while True:
#         try:
#             fraction = input("Fraction: ")
#             x,y = fraction.split('/')
#             x = int(x)
#             y = int(y)
#             number_check(x,y)
#             percent = convert(x,y)
#             output(percent)
#             break
#         except(ValueError, ZeroDivisionError):
#             continue


# def number_check(x,y):
#     if x < 0 or y < 0:
#         raise ValueError("Values must pe positive")
#     if y == 0:
#         raise ZeroDivisionError
#     if x > y:
#         raise ValueError(f"{x} is greater than {y}")



# def convert(x,y):
#     return round((x/y)*100)

# def output(percent):
#     if percent >= 99:
#         print("F")
#     elif percent <= 1:
#         print("E")
#     else:
#         print(f"{percent}%")

# def main():
#     while True:
#         try:
#             fraction = input("Fraction: ")
#             percent = convert(fraction)
#             print(gauge(percent))
#             break
#         except (ValueError, ZeroDivisionError):
#             continue


# def convert(fraction):
#     try:
#         x, y = fraction.split('/')
#         x = int(x)
#         y = int(y)
#     except ValueError:
#         # Non-integer input
#         raise ValueError

#     if y == 0:
#         raise ZeroDivisionError
#     if x > y:
#         raise ValueError

#     percent = round((x / y) * 100)
#     return percent


# def gauge(percentage):
#     if percentage <= 1:
#         return "E"
#     elif percentage >= 99:
#         return "F"
#     else:
#         return f"{percentage}%"


# if __name__ == "__main__":
#     main()
