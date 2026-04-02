class Solution:
    '''
    1. Create a hashmap to store the count of each element in the hashmap 
    and how many times it occurs

    2. Create a list of empty lists and map each element into a list, aka bucket, 
    depending on the value (frequency it occurs in the nums list)
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # map the frequency of each element to its value in dict
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        # create a list of buckets to sort the elements depending on frequendy
        buckets = [] 
        buckets = [[] for i in range(len(nums)+1)]

        for num, freq in freqMap.items():
            # add num to bucket 
            bucket = buckets[freq]
            bucket.append(num)


        # return the top k frequent elements 
        result = []

        for bucket in buckets[::-1]:
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result



        