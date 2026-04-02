class MinStack:

    def __init__(self):
        # create an empty array
        self.stack = []

    def push(self, val: int) -> None:
        # add element to top of stack
        self.stack.append(val)

    def pop(self) -> None:
        # remove top element aka the last element in the list
        lastElement = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return min(self.stack)
