"""
[[1,2],[1,4],[2,4]]
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals in ascending order by start time 
        intervals.sort()

        count = 0 
        prevEndTime = -float("inf")

        for interval in intervals:
            currStart = interval[0]
            currEnd = interval[1]

            # if currStart < prevEndTime, then it is overalapping 
            if currStart < prevEndTime:
                count += 1 
                prevEndTime = min(currEnd, prevEndTime)
            # otherwise it is not overlapping 
            else:
                prevEndTime = currEnd
                
        return count 
