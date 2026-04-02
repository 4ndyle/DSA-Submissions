class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos,speed] for pos,speed in zip(position,speed)]
        pair.sort(reverse=True)

        stack = []

        for pos,speed in pair:
            time = (target - pos) / speed
            stack.append(time)

            # check for collision of 2 cars, which creates a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
