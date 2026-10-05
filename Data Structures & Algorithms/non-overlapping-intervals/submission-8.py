"""
Find the total number of intervals that are not overlapping 

return len(intervals) - non-overlapping 
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0 
        prevEndTime = -float("inf")

        for currInterval in intervals:
            if prevEndTime > currInterval[0]:
                prevEndTime = min(prevEndTime, currInterval[1])
                count += 1
            else:
                prevEndTime = currInterval[1]
        
        return count