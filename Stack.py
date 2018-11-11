class Stack:
    def __init__(self):
        self.content = []

    def isEmpty(self):
        if len(self.content):
            return False
        else:
            return True

    def push(self, x):
        self.content.append(x)

    def pop(self):
        self.content.pop()

    def top(self):
        print(self.content[0])

    def bottom(self):
        print(self.content[len(self.content) - 1])
