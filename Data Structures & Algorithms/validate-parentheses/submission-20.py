"""

"""

class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = [] 

        for symbol in s: 
            if symbol not in parenMap: 
                stack.append(symbol)
            else:
                if stack and stack[-1] == parenMap[symbol]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
