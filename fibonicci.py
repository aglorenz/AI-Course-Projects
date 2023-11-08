def fibonacci_series(n):
    i, j = 0, 1
    series = []
    while i <= n:
        series.append(i)
        i, j = j, i + j
    return series

n = 8
print(fibonacci_series(n))
