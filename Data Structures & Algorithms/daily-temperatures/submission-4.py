"""
Input:
    - List[int] : temperature 
Output:
    - List[int] : where output[i] number of days until a warmer temperature appears in future 

Plan:
Add each element onto a stack until we encounter a element that is greater than the 
the top of the stack as a pair (value, index)

When an element is greater than the top of the stack:
set the output[index] = currElementIndex - index

temperatures = [30,38,30,36,35,40,28]

top of stack:
(38, 1)
(30,0)
found temperature greater
output[0] = 1 - 0

top of stack:
(35,4)
(36,3)
(30,2)
(38,1)
found element greater (40,5)
pop each element that is less than 40
output[4] = 5 - 4
output[3] = 5 - 3
output[2] = 5 - 2
output[1] = 5 - 1
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        # create stack to store temperature as tuples
        stack = []

        for i in range(len(temperatures)):
            currTemp = temperatures[i]

            # add temp to stack when there are no temperatures or when the top stack temp is >= the current temp
            if len(stack) == 0:
                print(f"appending ({currTemp}, {i}) to stack")
                print(stack)
                stack.append((currTemp, i))
                continue
            
            # pop from the stack while the current temp is greater than the top stack temp
            while stack and stack[-1][0] < currTemp:
                stackTemperature, stackIndex = stack.pop()

                output[stackIndex] = i - stackIndex

            stack.append((currTemp,i))

        return output







