from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # brute force is checking every row against every column

        # r = len(grid)
        # c = len(grid[0])
        # ans = 0
        # # O(N^3) tho
        # for i in range(r):
        #     for j in range(c):
        #         # check row against individual columns
        #         row = grid[i]
        #         # col is like, grid[all of r][j]? 
        #         # * 
        #         col = [grid[k][j] for k in range(r)]

        #         # then check if row == col, if yes, increment ans
        #         if row == col:
        #             ans += 1

        # return ans

        # * more efficient at O(N^2): 
        rows = Counter(tuple(row) for row in grid) # each row can be compared many times so store in dict, value is how many times that row appears
        ans = 0
        n = len(grid) # oh also it's n x n so only need one var for it

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n)) # n columns, each column build is O(N), so also O(N^2)
            ans += rows[col] # dict lookup is O(1) on avg
            # basically matching the col to whether shows up in rows, 0 if not, also takes care of multiple matches
    
        return ans