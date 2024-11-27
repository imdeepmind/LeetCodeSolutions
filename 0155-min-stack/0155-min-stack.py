class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = float('inf')
        
    def push(self, val: int) -> None:
        self.minValue = min(self.minValue, val)

        self.stack.append((val, self.minValue))

    def pop(self) -> None:
        self.stack.pop()

        if not self.stack:
            self.minValue = float('inf')
        else:
            self.minValue = self.stack[-1][1]

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()