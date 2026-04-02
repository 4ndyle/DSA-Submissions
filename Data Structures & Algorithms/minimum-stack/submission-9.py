
"""
All elements should run in O(1) time 

Stack:
0
2
1


objective:
keep track of the min number in stack and return in O(1) time 

Plan: Create a new stack to keep track of min elements
    - if the min element is popped, then pop from the min stack
    - otherwise, we can reference this stack to find the min element

"""

class MinStack:

    def __init__(self):
        # initializes a stack object 
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # push element val onto the top of the stack
        self.stack.append(val)

        # update the min stack
        if not self.minStack:
            self.minStack.append(val)
        else:
            if self.minStack[-1] >= val:
                self.minStack.append(val)

    def pop(self) -> None:
        # remove element on the top of stack
        elementRemoved = self.stack.pop()

        if self.minStack and elementRemoved == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        # return element on top of the stack 
        return self.stack[-1]

    def getMin(self) -> int:
        # return the min element of the stack
        return self.minStack[-1]


