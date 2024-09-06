# 1. Basic arithmetic operations func
def operations(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        print("Invalid operation")


def calc(op, x, y):
    return {
            '+': lambda: x + y,
            '-': lambda: x - y
            }.get(op) ()


# 2. Implement a Fibonacci Sequence Generator.
def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

for _ in range(10):
    print(next(fib_gen))



# 3. Checks whether a given string is a palindrome
def is_palindrome(str):
    str = str.replace(" ", "").lower()

    return str == str[::-1]
