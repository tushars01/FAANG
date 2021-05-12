n = int(input("Enter the number "))


def fib_rec(n):
    if n == 1 or n == 0:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_rec(n))
