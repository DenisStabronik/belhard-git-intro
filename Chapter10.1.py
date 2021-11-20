def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, "равно", b)
    else:
        print(b, 'максимально')

x = 5
y = 2
printMax(x,y)
