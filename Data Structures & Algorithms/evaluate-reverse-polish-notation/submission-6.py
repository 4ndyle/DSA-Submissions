class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 1:
            return int(tokens[0])

        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            # check if token is an operator or not
            if token in operators:
                result = 0
                secondNum = int(stack.pop())
                firstNum = int(stack.pop())

                # operate on two numbers
                if token == '+':
                    result = firstNum + secondNum
                elif token == '-':
                    result = firstNum - secondNum
                elif token == '*':
                    result = firstNum * secondNum
                else:
                    result = firstNum / secondNum

                stack.append(result)
            else:  
                stack.append(token)

        print(stack)
        print(stack[0])

        return int(stack[0])
