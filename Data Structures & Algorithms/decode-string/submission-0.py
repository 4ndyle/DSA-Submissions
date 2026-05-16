class Solution:
    def decodeString(self, s: str) -> str:
        currString = ""
        currNumberString = ""
        stack = []

        for char in s:
            # if the current number is a digit, update the number
            if char.isdigit():
                currNumberString += char
            # if the current character is a "[", add the current number and string to the stack
            elif char == "[":
                stack.append(currString)
                currNumber = int(currNumberString) if currNumberString else 0
                stack.append(currNumber)

                currString = ""
                currNumberString = ""

            # if the current character is a "]", pop number and string from stack and calculate
            elif char == "]":
                repeat = stack.pop()
                prevString = stack.pop()

                newString = prevString + repeat * currString
                currString = newString
                currNumberString = ""
            # if the current charcater is a letter, add the letter to currString
            else:
                currString += char
                
        return currString