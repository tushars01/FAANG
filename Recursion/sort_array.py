arr = [5, 2, 3, 6, 11]
i = 0
print(min(arr))

def sort_array(arr, i):
    if len(arr) == 1:
        return arr
    arr[i] = min(arr)
    i = i + 1
    return sort_array(arr[i:], i)
print(arr)
print(sort_array(arr,i))