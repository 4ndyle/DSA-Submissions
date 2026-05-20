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
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            currTemp = temperatures[i]

            # update the number fo days to wait for each day with a temprature < currTemp
            while stack and currTemp > temperatures[stack[-1]]:
                prevTempIndex = stack.pop()
                numberOfDays = i - prevTempIndex

                result[prevTempIndex] = numberOfDays

            stack.append(i)

        return result







