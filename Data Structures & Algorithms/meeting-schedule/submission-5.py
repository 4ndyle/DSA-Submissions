"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the intervals in ascending order by start time 
        intervals.sort(key = lambda interval : interval.start)
        
        # iterate through each interval and keep track of the prev end time 
        prevEndTime = 0

        for interval in intervals:
            currStart = interval.start
            currEnd = interval.end

            if currStart < prevEndTime:
                return False
            else:
                prevEndTime = currEnd

        return True