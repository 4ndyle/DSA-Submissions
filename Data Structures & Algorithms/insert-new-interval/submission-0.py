class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        # add all intervals with an end time < newInterval.start 
        index = 0 

        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        # Continue iterating through the intervals and combine all overlapping intervals  with newInterval
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newIntervalStart = min(newInterval[0], intervals[index][0])
            newIntervalEnd = max(newInterval[1], intervals[index][1])

            newInterval = [newIntervalStart, newIntervalEnd]
            index += 1

        # add the new interval to the list 
        result.append(newInterval)

        # add remaining intervals to the list 
        while index < len(intervals):
            result.append(intervals[index])
            index += 1

        return result