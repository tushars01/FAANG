from queue import LifoQueue
# arr = [1, 3, 2, 4]
arr = [4, 5, 2, 25]
vect = []
stack = []


n = len(arr)

for i in range(n-1, -1, -1):
    if len(stack) == 0:
        vect.append(-1)
    elif len(stack) != 0 and stack[-1] > arr[i]:
        vect.append(stack[-1])
    elif len(stack) != 0 and stack[-1] <= arr[i]:
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            vect.append(-1)
        else:
            vect.append(stack[-1])
    stack.append(arr[i])

vect.reverse()

print(vect)
