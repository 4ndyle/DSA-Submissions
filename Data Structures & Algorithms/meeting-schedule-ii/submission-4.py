"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

1. Sort the intervals 
2. Create 2 arrays keeping track of the start and end times 
3. Create a variable to keep track of maxMeetings and currMeetings
3. Use two pointers and iterate through the intervals
    - if the startTime < endTime:
        increment currMeetings count 
        update the maxMeetings count 
    - otherwise, there will be a meeting : 

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals in ascending order based on the start time 
        # create two arrays that hold the start time and end times 
        startTimes = []
        endTimes = []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)

        startTimes.sort()
        endTimes.sort()

        # create a pointer in each array and move pointers until end of start 
        startPointer = 0
        endPointer = 0
        
        maxMeetings = 0
        currMeetings = 0

        while startPointer < len(intervals):
            currStart = startTimes[startPointer]
            currEnd = endTimes[endPointer]

            # if the startTime < endTime, then we start a meeting up,
            if currStart < currEnd:
                currMeetings += 1
                maxMeetings = max(maxMeetings, currMeetings)
                
                startPointer += 1
            # otherwise, a meeting is going to be ending before we add the next start 
            else:
                currMeetings -= 1

                endPointer += 1

        return maxMeetings