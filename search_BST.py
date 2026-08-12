# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        # I mean it's just, finding that specific node.val == val, then return the subtree? 

        if not root:
            return null
        
        if root.val == val:
            return root
        
        # else subtree stuff
        # if root.left: 
        #     self.searchBST(root.left)
        # if root.right:
        #     self.searchBST(root.right)

        curr = root
        
        # or ig, it's a BST so we automatically know which way to go
        while curr and curr.val != val: 
            if curr.val > val: 
                curr = curr.left # narrow search to the left b/c val is less than
            else:
                curr = curr.right
        
        # and it ends if curr.val == val
        return curr