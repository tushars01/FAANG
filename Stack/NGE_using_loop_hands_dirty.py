# arr = [4, 5, 2, 25]
# arr = [4,3,2,1]
# arr = [5, 10, 15, 20]
arr = [2, 1, 5, 2, 1, 1, 10, 3, 1, 2, 5, 10]

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
        # k += 1
    k += 1
    NGE[k] = next_
    # if j == len(arr):
    #     k += 1

# print(NGE)
# for i in range(0, len(arr)):
#     if arr[i] > NGE[i]:
#         NGE[i] = -1
print("After")
print(NGE)
