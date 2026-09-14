class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals in ascneding order by start time
        intervals.sort(key = lambda x : x[0])

        # create list to store results
        results = []

        # merge intervals 
        for i in range(len(intervals)):
            currInterval = intervals[i]

            if not results:
                results.append(currInterval)
            else:
                prevInterval = results[-1]

                if prevInterval[1] >= currInterval[0]:
                    results[-1][1] = max(currInterval[1], prevInterval[1])
                else:
                    newInterval = [currInterval[0], currInterval[1]]
                    results.append(newInterval)

        return results