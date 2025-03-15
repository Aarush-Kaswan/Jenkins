def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Print first 10 Fibonacci numbers
print([fibonacci_recursive(i) for i in range(10)])
