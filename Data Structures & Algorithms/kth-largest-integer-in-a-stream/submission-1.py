"""
1. Create a list and sort input list every time a new number is inserted 
    constructor:
        - time: O(n logn)
        - space: O(n)
    
    add:
        - time: O(n)
        - space: O(1)
2. Create a heap of length k to store numbers
    constructor:
        - time: O(n logk)
        - space: O(k)
    
    add:
        - time: O(log k)
        - space: O(1)
"""

import heapq

class KthLargest:
    """
    Input: 
        - int k
        - List[int] nums
    Output:
        - N/A
    Constraints:
        - possible values of k: [1,1000]
        - possible values of nums: [-1000,1000]
        - possible length of nums: [0,1000]
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        # pop elemnts until heap is length k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    """
    Input:
        - int val
    Output:
        - int : kth largest element in list
    Constraints:
        - possible values of val: [-1000,1000]
        - there will always be at least k integers in the stream 
    """
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # update heap if length > k 
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
