class Stack:
    def __init__(self):
        self.__items = []


    def push(self,data):
        self.__items.append(data)


    def pop(self):
        if self.__items:
            return self.__items.pop()
        return None

    def peek(self):
        if self.__items:
            return self.__items[-1]
        return None



stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())

