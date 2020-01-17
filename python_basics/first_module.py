# first_module.py
def add(a, b):
    c = a + b
    return c, "+"
    
def subtract(a, b):
    c = a - b
    return c, "-"

def multiply(a, b):
    c = a * b
    return c, "*"

def divide(a, b):
    c = a / b
    return c, "/"

if __name__ == "__main__":
    a = 5
    b = 3
    answer, symbol = add(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = subtract(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    x = 47
    y = 7
    answer, symbol = add(x, y)
    print("{} {} {} = {}".format(x, symbol, y, answer))
    answer, symbol = subtract(x, y)
    print("{} {} {} = {}".format(x, symbol, y, answer))
    answer, symbol = multiply(x, y)
    print("{} {} {} = {}".format(x, symbol, y, answer))
    answer, symbol = divide(x, y)
    print("{} {} {} = {}".format(x, symbol, y, answer))