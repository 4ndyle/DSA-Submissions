class MinStack:

    def __init__(self):
        # create an empty array
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # add element to top of stack and min to second stack
        self.stack.append(val)

        
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))


    def pop(self) -> None:
        # remove top element aka the last element in the list
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
