n = int(input("Enter the number "))
arr = [0] * (n + 1)
print(arr)


def fib_rec_improved(n, arr):
    if n == 1 or n == 0:
        arr[n] = 1
        return arr[n]
    if arr[n] > 0:
        return arr[n]
    arr[n] = fib_rec_improved(n - 1, arr) + fib_rec_improved(n - 2, arr)
    output = arr[n]
    return output


print(fib_rec_improved(n, arr))
print(arr)
