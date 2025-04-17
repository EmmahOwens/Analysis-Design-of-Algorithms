def fib(n, memo = None):
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]
result = fib(5)
print("Fibonacci number at position 5 is ", result)
