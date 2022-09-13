def test_fib_func():
    print("Result should be 0\n  Result: {}".format(fibonacci(0)))
    print("Result should be 1\n  Result: {}".format(fibonacci(1)))
    print("Result should be 2\n  Result: {}".format(fibonacci(3)))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    test_fib_func()