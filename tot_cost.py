import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        
        # each session, choose from first candidates workers or the last candidates workers, then need to remove them from the list
        # like need to keep order of costs to check first vs last candidates? 

        # 2 min heaps, one for left, one for right, I'm guessing length of candidates, then just pick the smallests from each and compare, tie breaker is pick the left one
        left_heap = []
        right_heap = [] 
        cost = 0
        # * yea use ptrs to double check when stop
        left_ptr = 0
        right_ptr = len(costs) - 1

        # set up the two heaps, length candidates left and right
        while left_ptr < candidates and left_ptr <= right_ptr: 
            heapq.heappush(left_heap, costs[left_ptr])
            left_ptr += 1
        
        # * this condition for right ptr
        while right_ptr >= len(costs) - candidates and right_ptr >= left_ptr:
            heapq.heappush(right_heap, costs[right_ptr])
            right_ptr -= 1

        # heap peek then heap pop the correct one?, cost += it, then add new elmt to that heap <- and make sure final num is k

        for _ in range(k):
            if left_heap and (not right_heap or left_heap[0] <= right_heap[0]):
                # * pick from left heap if no right heap, this way instead of heap peek, and always from the left if tie
                cost += heapq.heappop(left_heap)

                if left_ptr <= right_ptr:
                    heapq.heappush(left_heap, costs[left_ptr]) # maintaining left heap when able to
                    left_ptr += 1        
            else: # same but for the right heap
                cost += heapq.heappop(right_heap)

                if left_ptr <= right_ptr:
                    heapq.heappush(right_heap, costs[right_ptr])
                    right_ptr -= 1 # increment to the left instead

        return cost