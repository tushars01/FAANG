arr = [4, 2, 3, 1]
stack = []
vect = []

for i in range(0, len(arr)):
    if len(stack) == 0:
        vect.append(-1)

    elif len(stack) != 0 and stack[-1] > arr[i]:
        vect.append(stack[-1])

    elif len(stack) != 0 and stack[-1] <= arr[i]:
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            vect.append(-1)
        if stack[-1] > arr[i]:
            vect.append(stack[-1])
    stack.append(arr[i])

print(vect)
