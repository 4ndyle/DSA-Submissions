class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEndTime = -float("infinity")
        count = 0 

        for currInterval in intervals:
            if currInterval[0] < prevEndTime:
                count += 1
                prevEndTime = min(prevEndTime, currInterval[1])
            else:
                prevEndTime = currInterval[1]

        return count
