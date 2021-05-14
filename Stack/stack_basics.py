
class Stack():
    def __init__(self, li):
        self.top = -1
        self.li = []

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        if self.top < 0:
            return True
        return False

    def is_full(self):
        if self.top == len(self.li) - 1
            return True
        return False
