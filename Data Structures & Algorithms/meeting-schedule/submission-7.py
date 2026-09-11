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
Output
    - bool : if person can add all meetings to their schedule without conflicts
Constraints:
    - Length of intervals: [0,500]
    - Values of intervals: [0,1000000]

Plan:
1. Sort the intervals in ascending order based on the start time
2. for in in range(len(intervals)):
        if the end time of the current interval > start time of next interval, then return False
3. Return true (if all intervals do not have conflicting start and end times)
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False

        return True