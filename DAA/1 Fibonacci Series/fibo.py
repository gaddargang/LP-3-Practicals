import timeit

def fibonacci(n):
    """Non-recursive Fibonacci function"""
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]

def fibonacci_recursive(n):
    """Recursive Fibonacci function"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]

N = int(input("Enter the number of terms in the series: "))

RUNS = 1
fib_list = [0] * (N + 1)
fib_list[0] = 0
fib_list[1] = 1
print("Fibonacci non-recursive:")
for i in range(N):
    print(fibonacci(i), end=' ')  # Print numbers only
print("\nTime:", f'{timeit.timeit("fibonacci(N)", setup=f"from __main__ import fibonacci;N={N}", number=RUNS):5f}', "O(n)\tSpace: O(1)")

fib_recur_list = [0] * (N + 1)
fib_recur_list[0] = 0
fib_recur_list[1] = 1
print("\nFibonacci recursive:")
for i in range(N):
    print(fibonacci_recursive(i), end=' ')  # Print numbers only
print("\nTime:", f'{timeit.timeit("fibonacci_recursive(N)", setup=f"from __main__ import fibonacci_recursive;N={N}", number=RUNS):5f}', "O(2^n)\tSpace: O(n)")
