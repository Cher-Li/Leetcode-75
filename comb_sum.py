class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        result = []
        # sorta backtracking vibes where you have a tree of numbers, keep appending a bigger num until reach length k and check if equal n
        # possibly a visited set to keep track of which nums are used but maybe not an issue if just keep appending a bigger num
        # separate dfs func? like, after including a number, want to find combinations of k - 1 that sum up to n - that first num? 

        def backtrack(start_num, remaining):
            # remaining = remaining sum until target

            if remaining == 0 and len(cur_combo) == k:
                # found a combo
                result.append(cur_combo[:]) # * copy of combo
                return
            
            # * "pruning" conditions
            if start_num > 9 or start_num > remaining or len(cur_combo) >= k:
                return

            # different choices: 
            # 1. include the number
            cur_combo.append(start_num)
            backtrack(start_num + 1, remaining - start_num)

            # backtrack by removing num
            cur_combo.pop()

            # 2. skip cur num and move on
            backtrack(start_num + 1, remaining)
        
        cur_combo = []
        backtrack(1, n) # dfs from the starting num of 1 with sum == n

        return result