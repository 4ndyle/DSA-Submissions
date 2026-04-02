class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # pair of [temperature,index]
        result = [0] * len(temperatures)

        for index, val in enumerate(temperatures):
            # pop from stack while current temperature is greater than prior temperatures
            while stack and val > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex

            stack.append((val, index))

        return result
