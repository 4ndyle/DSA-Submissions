"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Input:
    - List[Interval] : intervals 
Output:
    - bool : schedule has any conflicts or not 
constraints:
    - length of intervals: [0,500]
    - range of values: [0,1000000]
    - intervals[i].start < intervals[i].end 

empty list: return True

Plan: 
1. Sort the list in ascending order by the start time 
2. Iterate through each interval and check if the current interval start 
is less than the previous intervals end time 
    - if the current interval's start < prev end time, return False 
3. Return True if all intervals do not conflict 
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # sort the list of intervals by the start time 
        intervals.sort(key = lambda currInterval: currInterval.start)
        
        for i in range(1, len(intervals)):
            currInterval = intervals[i]

            # check if the current interval start < prev interval end 
            if currInterval.start < intervals[i-1].end:
                return False

        return True





