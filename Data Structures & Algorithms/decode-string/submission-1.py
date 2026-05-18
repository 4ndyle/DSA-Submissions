class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                # calcualate the repeated string
                phrase = ""

                while stack and stack[-1] != '[':
                    phrase = stack.pop() + phrase

                # consume the "["
                stack.pop()

                # find the number
                numberString = ""

                while stack and stack[-1].isdigit():
                    numberString = stack.pop() + numberString

                result = int(numberString) * phrase
                stack.append(result)
            else:
                stack.append(char)
        
        return ''.join(stack)
    