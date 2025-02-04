def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(10))
    print(factorial(15))
    print(factorial(20))
    print(factorial(25))