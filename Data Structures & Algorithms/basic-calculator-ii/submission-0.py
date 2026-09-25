class Solution:
    def calculate(self, s: str) -> int:
        stack = [] 
        operator = '+'
        num = 0
        s += '+'

        for char in s:
            if char == ' ':
                continue 

            if char.isdigit(): 
                num = num * 10 + int(char)
                continue 
            
            # operators 
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num))

            num = 0
            operator = char

        return sum(stack)