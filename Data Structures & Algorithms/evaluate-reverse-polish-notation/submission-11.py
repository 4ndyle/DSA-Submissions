"""
Input: 
    - List[str]
Output: 
    - Int : representation of the integer and operations applied 
Constraints:
    - operands may be int or results of other operations 
    - operators include '+', '-', '*', '/'
    - assume that division between integers always truncates toward zero

    - 1 <= tokens.length <= 1000
Edge Cases:

Plan: Use a stack and iterate though the list of tokens. When we encounter a number,
add it to the stack and when we encounter a operator, pop the two latest numbers
from the stack and apply the operator for them and add it back onto the stack. At the end, 
return the number left in the stack
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operations  = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operations:
                numStack.append(int(token))
                print(f"adding {token}")
            else:
                num2 = numStack.pop()
                num1 = numStack.pop()

                match token:
                    case "+": res = num1 + num2
                    case "-": res = num1 - num2
                    case "*": res = num1 * num2
                    case "/": res = int(num1/num2)

                numStack.append(res)

            print(numStack)

        return numStack.pop()