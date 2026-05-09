class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals in asecnding order based on the start interval 
        intervals.sort()

        # Create a list to hold the results of the sorted intervals
        result = []
        prevEndTime = 0 

        # Iterate through each interval and keep track of the end time of the previous intervals
        for interval in intervals:
            currStart = interval[0]
            currEndTime = interval[1]

            # merge or append the current interval based 
            if result and currStart <= prevEndTime:
                result[-1][1] = max(currEndTime, prevEndTime)
            else:
                result.append(interval)

            # update previous end time
            prevEndTime = max(currEndTime, prevEndTime)

        return result