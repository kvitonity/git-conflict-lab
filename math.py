def pow(x):
    return x ** 2

# Returns square root of a number
def sqrt(x):
    return x ** 0.5

def cube(x):
    return x ** 3

# Returns x ** n
def powN(x, n):
    return x ** n

def Factorial(n):
    f = 1
    for i in range(n):
        f = f * (i + 1)
    return f
