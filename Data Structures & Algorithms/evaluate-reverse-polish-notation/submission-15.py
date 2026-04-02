
"""
Input:
    - List[str] : tokens
Output:
    - int : evaluation of the expression of all tokens 

Example 1:
tokens = ["1","2","+","3","*","4","-"]
output: 5

1, 2, + -> 3

3, 3, * -> 9

9, 4, - -> 5

Goal: Keep track of the calculation from the previous step

stack:

iteration 0:
stack = [1,2]
operation = "+"

pop last 2 elements on stack and perform the operation, add back onto stack
1 + 2 = 3, append 3 onto stack

iteration 1:
[3,3]
*

3 * 3 = 9, append to stack

iteration 2:
[9,4]
-

9 - 4 = 5, return top of stack
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack to keep track of numbers
        stack = []
        operators = {"+", "-", "/", "*"}

        for token in tokens:
            # if the token is not a operator, append to stack
            if token not in operators:
                stack.append(int(token))
            # otherwise, pop 2 numbers off the stack and apply the operator, and add back onto stack
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                match token:
                    case "+": 
                        stack.append(num1 + num2) 
                    case "-": 
                        stack.append(num1 - num2) 
                    case "*": 
                        stack.append(num1 * num2) 
                    case _: 
                        stack.append(int(num1 / num2))

        return stack.pop()




