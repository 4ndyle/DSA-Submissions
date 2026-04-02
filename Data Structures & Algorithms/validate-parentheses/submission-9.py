class Solution:
    def isValid(self, s: str) -> bool:

        symbol = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s: 
            # pop the stack if the current char is a closing symbol, matches with the opening symbol, and the stack is not empty 
            if char in symbol.keys() and len(stack) > 0 and stack[-1] == symbol[char]:
                stack.pop()
            else: 
                stack.append(char)

        return len(stack) == 0