class MinStack:

    def __init__(self):
        self.stack = []        # main stack to store all elements
        self.min_stack = []    # auxiliary stack to store the minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's the first element or smaller/equal than current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # Output: -3
obj.pop()
print(obj.top())     # Output: 0
print(obj.getMin())  # Output: -2


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
