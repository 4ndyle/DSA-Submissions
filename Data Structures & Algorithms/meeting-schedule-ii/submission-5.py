"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # create a sorted list of start and end times 
        startTimes = [] 
        endTimes = [] 

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)

        startTimes.sort()
        endTimes.sort()

        # create pointers for start/end times and count variable 
        # increment when meeting starts, decrement when meetings ends 
        count = 0 
        maxCount = 0
        startIndex = 0
        endIndex = 0 

        while startIndex < len(startTimes):
            # meeting room starts
            if startTimes[startIndex] < endTimes[endIndex]:
                count += 1
                startIndex += 1

                maxCount = max(count, maxCount)
            # meeting room ends before a new meeting starts 
            else:
                count -= 1
                endIndex += 1

        return maxCount 



