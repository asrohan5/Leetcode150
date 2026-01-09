class MinStack:

    def __init__(self):
        self.stack = []  # Stores all elements [value, current_min]
        # self.minStack = [] # Alternative: parallel stack for mins

    def push(self, val: int) -> None:
        if not self.stack:
            # First element, it's the min
            self.stack.append([val, val])
        else:
            # Get current min, compare with new val, push both
            current_min = self.stack[-1][1]
            new_min = min(val, current_min)
            self.stack.append([val, new_min])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0] # Return the actual value

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1] # Return the current minimum
