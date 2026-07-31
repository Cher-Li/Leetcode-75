# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # I guess something like depth first search and just keep track of the deepest depth? 

        if not root:
            return 0

        # max_depth = 0
        # visited = set()
        # self.dfs(root, max_depth, visited)
        # * it's a binary tree so visited set not necessary, also max_depth would need to be global

        # max_depth = self.dfs(root, 0)
        # return max_depth

        # * or this recursive method where depth is 1 + max of depth of each child
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
    
    # def dfs(self, node, max_depth): # technically current_depth and at the end it's max
    #     # visited.add(node)

    #     if not node: 
    #         return max_depth
        
    #     max_depth += 1

    #     # if node.left:
    #     #     self.dfs(node.left, max_depth, visited)
    #     # if node.right: 
    #     #     self.dfs(node.right, max_depth, visited)

    #     # * basically directly return the deepest route each time
    #     return max(self.dfs(node.left, max_depth), self.dfs(node.right, max_depth))