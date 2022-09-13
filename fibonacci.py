def test_fib_func(n):
    print(test_func(1))
    print(fib(0))
    print(fib(1))
    print(fib(3))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n

if __name__ == "__main__":
    test_fib_func()