"""
Input:
    - List[int] : position 
        - position[i] is the position of the ith car (miles)
    - List[int] : speed
        - speed of the ith (miles per hour)
    - int : target (miles)

Rules:
1. Car cannot pass another car, it can catch up and match speed (form a fleet)
2. Car fleet - set of cars driving the same position and speed (single cars count)
3. If a car catches up to a fleet when at destination, it is apart of the fleet

Output:
    - int : number of different car fleets that will arrive at the destination 


"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip the position and speed to keep track of their pairs 
        zipped = list(zip(position, speed))

        # sort the cars based on their position in descending order 
        zipped.sort()
        stack = []

        # calculate the speed for each car
        for position, speed in zipped:
            distanceLeft = target - position
            timeLeft = distanceLeft / speed

            stack.append(timeLeft)

        print(stack)
        
        fleets = 0 

        while stack:
            topFleetSpeed = stack.pop()

            while stack and stack[-1] <= topFleetSpeed:
                stack.pop()

            fleets += 1

        return fleets
