import sys

# error handling
# sys.exit() quits the program and prints an exit statement
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# nametag functionality
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)


