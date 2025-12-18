def main():
    equation = input("Equation: ")
    x, operator, y = equation.split(" ")
    x = float(x)
    y = float(y)

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "/":
        result = x / y
    elif operator == "*":
        result = x * y
    else:
        print("not a valid equation")

    print (result)

main()
