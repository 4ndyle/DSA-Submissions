"""
Find the total number of intervals that are not overlapping 

return len(intervals) - non-overlapping 
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0 
        prevEndTime = -float("inf")

        for i in range(len(intervals)):
            currStart, currEnd = intervals[i]

            # skip interval if overlapping 
            if i != 0 and prevEndTime > currStart:
                prevEndTime = min(prevEndTime, currEnd)
                continue 

            prevEndTime = currEnd
            count += 1
        
        # print(count)
        return len(intervals) - count