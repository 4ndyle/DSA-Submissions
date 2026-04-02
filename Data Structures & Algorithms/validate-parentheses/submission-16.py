class Solution:
    def isValid(self, s: str) -> bool:
        openingParenDict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for paren in s:

            if paren in openingParenDict:
                if stack and openingParenDict[paren] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)

        return len(stack) == 0