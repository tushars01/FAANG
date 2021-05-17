arr = [1, 3, 2, 4]
k = -1
NGL = [-10]*len(arr)

for i in range(0, len(arr)):
    next_ = -1

    for j in range(0, i):
        if arr[j] > arr[i]:
            next_ = arr[j]
    k += 1
    NGL[k] = next_

print(NGL)
