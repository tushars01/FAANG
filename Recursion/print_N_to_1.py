n = int(input("Enter the number "))


def print_1_to_n(n):
    if n == 0:
        return
    print(n, end=' ')
    print_1_to_n(n - 1)


print_1_to_n(n)
