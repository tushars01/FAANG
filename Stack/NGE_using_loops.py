# arr = [4, 5, 2, 25]
# arr = [4,3,2,1]
# arr = [5, 10, 15, 20]
# arr = [2, 1, 5, 2, 1, 1, 10, 3, 1, 2, 5, 10]
# arr = [2, 1, 5, 2, 1, 1, 10, 3, 1, 2, 5, 11]
# arr = [11, 13, 3, 21]

arr = [11, 13, 21, 3]
NGE = [-10] * len(arr)
k = -1

print("Before ")
print(arr)

for i in range(0, len(arr)):
    next_ = -1
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            next_ = arr[j]
            break

    k += 1
    NGE[k] = next_

print("After")
print(NGE)
