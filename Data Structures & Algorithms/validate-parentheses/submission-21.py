"""

"""

class Solution:
    def isValid(self, s: str) -> bool:
        parenMatch = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for paren in s:
            if paren in parenMatch.values():
                stack.append(paren)
            else:
                if stack and stack[-1] == parenMatch[paren]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
