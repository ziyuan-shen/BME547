# basics.py
x = input("Enter a letter: ")
print("You entered {}.".format(x))
if x == 'a':
    print("Add")
    a = 1
    b = 2
    c = a + b
    print("{} + {} = {}".format(a, b, c))
elif x == "s":
    print("Subtract")
    a = 1
    b = 2
    c = a - b
    print("{} - {} = {}".format(a, b, c))
elif x == "m":
    print("Multiply")
    a = 1
    b = 2
    c = a * b
    print("{} * {} = {}".format(a, b))
elif x == "d":
    print("Divide")
    a = 1
    b = 2
    c = a / b
    print("{} / {} = {}".format(a, b))
else:
    print("{} not recognized".format(x))
print("Finished")