class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)


    def pop(self) -> int:
        '''
        time complexity is O(1) amortised

        '''
        if self.empty():
            return None

        self.populate_s2_if_empty()

        return self.s2.pop()

    def populate_s2_if_empty(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())


    def peek(self) -> int:
        if self.empty():
            return None

        self.populate_s2_if_empty()

        return self.s2[-1]


    def empty(self) -> bool:
        if self.s1 or self.s2:
            return False

        return True


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(f"peek = {obj.peek()}")
obj.push(1)
obj.push(2)
obj.push(3)
print(f"pop = {obj.pop()}")
print(f"peek = {obj.peek()}")
print(obj.empty())