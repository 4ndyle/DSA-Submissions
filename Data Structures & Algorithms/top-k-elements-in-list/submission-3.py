class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count for each element in the list
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # create bucket list and place num in bucket where the index represents the num frequency count
        bucket = [[] for i in range(len(nums))]

        for key, val in frequency.items():  
            bucket[val-1].append(key)

        print(bucket)

        res = []
        for i in range(len(nums)-1, -1, -1):
            if not bucket[i]:
                continue

            for num in bucket[i]:
                if k <= 0:
                    return res
                else:
                    res.append(num)
                    k -= 1

        return res

        