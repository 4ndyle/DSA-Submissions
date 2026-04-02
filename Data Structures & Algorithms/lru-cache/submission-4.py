"""
Example:
LRUCache lRUCache = new LRUCache(2);
{}

lRUCache.put(1, 10);  // cache: {1=10}
{
    1 : 10
}

lRUCache.get(1);      // return 10

lRUCache.put(2, 20);  // cache: {1=10, 2=20}
{
    1 : 10,
    2 : 20
}

lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
{
    2 : 20
    3 : 30
}

pop the first item in the dict. 

lRUCache.get(2);      // returns 20 
{
    3 : 30
    2 : 20
}

move 2 : 20 to the end of the dict since it was just used

lRUCache.get(1);      // return -1 (not found)
"""

from collections import OrderedDict

class LRUCache:

    # intialize the lru cache with a size of capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    # return value corresponding to the key
    # will be moved to the most recently used if key is called
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        print(f"accessed {key}")
        print(f"dict is now {self.cache}\n")
        return self.cache[key]

    # puts a new key with the value into the cache
    # will be most recently used when added to the cache
    """
    if the key exists -> update value
    otherwise -> add the key : val pair

    remove least recently used key when the size of cache > capacity
    """
    def put(self, key: int, value: int) -> None:
        # remove the first item in the cache if the capacity is greater
        print(f"adding {key} : {value}")
        self.cache[key] = value
        self.cache.move_to_end(key)
        print(self.cache)

        if len(self.cache) > self.capacity:
            poppedItem = self.cache.popitem(last=False)
            print(f"popped {poppedItem}")
        
        print(self.cache)
        print()





