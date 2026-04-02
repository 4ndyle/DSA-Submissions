"""

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # create a dict to map parenthesis to their corresponding parenthesis
        parenDict = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        # Iterate through each symbol
        for symbol in s:
            # if the symbol is a opening parenthesis, add it to the stack
            if symbol in parenDict.values():
                stack.append(symbol)
            # otherwise, if the symbol is a closing paraenthesis, check if it has a corresponding opening parenthesis
            else:
                if stack and stack[-1] == parenDict[symbol]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
