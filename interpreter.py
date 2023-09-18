def interpreter():
    expression = input("Expression: ").lower().strip()
    x, y, z = expression.split(" ")

    if y == "+":
        result = float(x) + float(z)
        print(result)
    elif y == "-":
        result = float(x) - float(z)
        print(result)
    elif y == "*":
        result = float(x) * float(z)
        print(result)
    elif y == "/":
        result = float(x) - float(z)
        print(result)

interpreter()
