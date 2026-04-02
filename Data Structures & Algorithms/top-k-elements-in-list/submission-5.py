class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count for each element in the list
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # create bucket list and place num in bucket where the index represents the num frequency count
        bucket = [[] for i in range(len(nums)+1)]

        for key, val in frequency.items():  
            bucket[val].append(key)

        print(bucket)

        res = []
        for bucketList in bucket[::-1]:

            for num in bucketList:
                res.append(num)

                if len(res) == k:
                    return res
                
        return res

        