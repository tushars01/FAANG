arr = [4, 5, 2, 10, 8]
NSL = [-10] * len(arr)

k = -1

for i in range(0, len(arr)):
    next_ = -1
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            next_ = arr[j]
            break
    k += 1
    NSL[k] = next_

print(NSL)