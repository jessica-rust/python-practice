def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


""" Concise Version """

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # return breaks you out of the loop AND returns the value
        except ValueError:
            pass # restarts the loop without actually giving an error



""" Less Concise """

# def get_int(prompt):
#     while True:
#         try:
#             x = int(input(prompt))
#             # break
#             # Since no errors can be raised by break,
#             # it can go before the execpt block and else wouldn't be needed
#         except ValueError:
#             print("not an integer")
#             # this actually tells the user what the problem is
#         else:
#             break
#             # placing the break here minimizes the lines that you are "trying"
#       return x


main()
