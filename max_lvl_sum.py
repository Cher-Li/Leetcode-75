# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
            
        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # update max_sum and max_level if the current level sum is strictly greater
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
                
            current_level += 1
            
        return max_level