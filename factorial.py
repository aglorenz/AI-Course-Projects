def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return (result)

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial(2))
print(factorial_recursive(5))
        