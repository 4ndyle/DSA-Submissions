class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        bracketMap = {
            '}' : '{',
            ']' : '[',
            ")" : '('
        }

        for char in s:

            # check whether top of stack matches with closing bracket and if it is a closing bracket 
            if len(stack) != 0 and char in bracketMap and bracketMap[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0