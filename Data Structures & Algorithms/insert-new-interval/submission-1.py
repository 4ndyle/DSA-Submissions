class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        inserted = False 

        # insert new interval into results in ascending order 
        for currInterval in intervals:
            if currInterval[0] >= newInterval[0]:
                newList.append(newInterval)
                inserted = True 

            newList.append(currInterval)

        if not inserted:
            newList.append(newInterval)

        # merge intervals that overlap 
        results = [] 

        for currInterval in newList:
            if results and results[-1][1] >= currInterval[0]:
                results[-1][1] = max(results[-1][1], currInterval[1])
            else:
                results.append(currInterval)

        return results