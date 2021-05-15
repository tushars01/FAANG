
class Stack():
    def __init__(self, li, max_size=10):
        self.top = -1
        self.li = []
        self.max_size = max_size

    def push(self, element):
        if self.is_full():
            return 'stack overflow, Can\'t add more element'
        self.top += 1
        self.li.append(element)
        return self.li[self.top]

    def pop(self):
        if self.is_empty():
            return 'stack underflow, Can\'t pop more element'

        # self.li.remove(element)
        element = self.li[self.top]
        self.li.pop()
        self.top -= 1
        return element

    def peek(self):
        if s.is_empty():
            return 'stack is empty, please add the element'
        return self.li[self.top]

    def is_empty(self):
        if self.top < 0:
            return True
        return False

    def is_full(self):
        if self.top > len(self.li) - 1:
            return True
        return False


li = []
max_size = 5
s = Stack(li, max_size)
while True:

    print('Enter the choice shown below: ')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. is empty')
    print('5 is full')
    inp = int(input())
    if inp == 1:
        element = int(input("Enter the element "))
        print(s.push(element))
    elif inp == 2:
        # element = int(input("Enter the element "))
        print(s.pop())
    elif inp == 3:
        print(s.peek())
    elif inp == 4:
        print(s.is_empty())
    elif inp == 5:
        print(s.is_full())
    else:
        print("Wrong choice, try again")
