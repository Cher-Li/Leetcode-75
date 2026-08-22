from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # ok this is similar to prev prob where bfs reaches until the end of the "map" 
        # queue = deque([(0, 0, 0)]) # row, col, min, currently assume first is 2
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        m, n = len(grid), len(grid[0]) # rows, cols

        # * also return -1 if when reach end of queue, there are still fresh oranges left, so need to decrement num fresh oranges when infect
        num_fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # yea just expanding from original idea of assuming start at 0,0
                
                elif grid[r][c] == 1:
                    num_fresh += 1
        
        # * edge case of no fresh oranges to begin with
        if num_fresh == 0:
            return 0
        
        minutes = 0

        while queue:
            r, c, minutes = queue.popleft()

            for d in directions: 
                # honestly it's more complicated than this since there could be multiple rotten oranges, so maybe first add all rotten oranges to the queue then keep expanding outwards? 
                new_row, new_col = r + d[0], c + d[1] 

                # if grid[new_row, new_col] == 1:
                #     # infect that orange
                #     grid[new_row, new_col] = 2 
                #     return minutes + 1 # <- not quite since need to continue

                # * checking boundaries first 
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1: 
                    grid[new_row][new_col] = 2
                    num_fresh -= 1 # * keep track of this then 
                    queue.append((new_row, new_col, minutes + 1)) # yea similar to prev prob just with minutes instead of steps
        
        # two cases, 1. infected all oranges and minutes is the correct ans, else -1 b/c impossible
        return minutes if num_fresh == 0 else -1