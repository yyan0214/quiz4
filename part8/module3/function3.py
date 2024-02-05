def generate_fibonacci(n):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        next_fib = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_fib)
    return fibonacci_series
