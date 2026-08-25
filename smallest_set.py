import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        # * self._, also keep track of cur and set to prevent duplicates
        self.current = 1 # <- keeps track of smallest int that hasn't been popped yet
        self.heap = []
        self.in_heap = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        # just pop the smallest int
        # also update cur / inheap? 
        # self.in_heap.remove(heapq.heappop(self.heap))
        
        if self.heap:
            # only one element so just pop that one
            # * return that smallest so just save it
            smallest = heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        
        # * otherwise it's the one the pointer is at then increment
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        # * num should be less than current, otherwise already in set
        if num < self.current and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)