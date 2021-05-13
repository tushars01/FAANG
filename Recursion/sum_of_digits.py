import math

n = int(input("Enter the number "))


def sum_of_digits(n):
    if n <= 0:
        return n
    return (n % 10) + sum_of_digits(math.floor(n / 10))


print(sum_of_digits(n))
