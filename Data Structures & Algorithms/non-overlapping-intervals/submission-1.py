class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)

        count = 0
        start = -float("inf")
        end = -float("inf")

        for interval in intervals:
            currStart = interval[0]
            currEnd = interval[1]

            if currStart < end:
                count += 1
                # If overlapping, keep the one that ends earlier to minimize future overlaps
                end = min(end, currEnd)
            else:
                # No overlap, update end to current interval's end
                end = currEnd
                start = currStart

        return count