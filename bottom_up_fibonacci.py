def bottom_up_fibonacci(n):
    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(2, n + 1):
        next = prev + curr
        print(f"Step {i - 1}: prev = {prev}, curr = {curr} → next = {next}")
        prev = curr
        curr = next

    return curr
result = bottom_up_fibonacci(5)
print("Fibonacci number at position 5 is :", result)
