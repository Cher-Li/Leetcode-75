# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def pathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: int
#         """
#         # this gives like, recursion vibes, the number of paths at the root would be num paths in left vs right root
#         # others nodes can be included as part of path, root doesn't have to? 
#         # straightforward is just, depth first search, literally count the number of paths where the sum is target? 

#         if not root:
#             return 0

#         # rn only deals w/ paths from root, paths could start anywhere
#         # self.ans = 0
#         # self.dfs(root, targetSum, 0)
#         # return self.ans

#         # * paths from root, then from root.left vs right which would continue going down
#         return (self.count_paths(root, targetSum) +  self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))

#     # def dfs(self, node, target, cur_sum): 
#     def count_paths(self, node, target): 
#         if not node:
#             return 0 # not just return b/c sum later on

#         # *
#         count = 0 # really counting in the function itself
#         if node.val == target:
#             count += 1
        
#         # cur_sum += node.val
#         # if cur_sum == target:
#         #     self.ans += 1

#         # self.dfs(node.left, target)
#         # self.dfs(node.right, target)

#         # and checking future paths starting from each node to see if make up the rest of the target sum
#         count += self.count_paths(node.left, target - node.val)
#         count += self.count_paths(node.right, target - node.val)

#         return count

# * O(N^2) -> O(N)
class Solution(object):
    def pathSum(self, root, targetSum):
        # hash map for optimized
        prefix_sums = {0 : 1} # <- frequency of sums seen so far

        def dfs(node, cur_sum):
            if not node:
                return 0
            
            cur_sum += node.val # similar to my first try
            ans = prefix_sums.get(cur_sum - targetSum, 0) 
            # checking if can match this cur sum with something in prefix_sums to reach target

            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1 # add cur sum to dict

            # recursion, like quite literally three parts again, focus on root, then check left vs right
            ans += dfs(node.left, cur_sum)
            ans += dfs(node.right, cur_sum)

            # * backtracking: 
            prefix_sums[cur_sum] -= 1

            return ans
        
        return dfs(root, 0)