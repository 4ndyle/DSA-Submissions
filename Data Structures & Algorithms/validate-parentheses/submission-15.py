"""
Input: 
    - string : s
Output: 
    - bool : if the string s is valid 
Valid if:
1. Every opemn bracket is closed by the same tyhpe of close bracket
2. Open brackets are closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type
Constraints:
    - 1 <= s.length <= 1000
Edge Cases:
    - "" -> return True

Plan: Use a stack and iterate through the while adding the parenthesis to the 
stack. If we encounter a closing parenthesis, check if it matches with the latest 
parenthesis and pop it off. If the stack is empty, we know it is valid, return True. 

Psuedo Code:
Create a dict to map the parenthesis 
{
    ')' : '('
    ']' : '['
    '}' : '{'
}

Create an empty stack

for currParenthesis in s:
    if current parenthesis is a opening parenthesis:
        add it to the stack
    else it is a closing parenthesis:
        if the parenthesis at the top is the matching opening parenthesis:
            pop it off the stack

if stack:
    return False

return True
"""

class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        parenStack = []

        for currParen in s:
            if currParen in paren:
                if parenStack and parenStack[-1] == paren[currParen]:
                    parenStack.pop()
                else:
                    return False
            else:
                parenStack.append(currParen)

        if parenStack:
            return False

        return True


        