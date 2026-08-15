# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        # 1. find the specific key
        # same as previous prob? 
        if not root:
            return None # * None instead of [] 
        
        # curr_node = root
        # while curr_node and curr_node.val != key:
        #     if curr_node.val > key: 
        #         curr_node = curr_node.left
        #     else: 
        #         curr_node = curr_node.right

        # * narrow down to the left vs right subtree each time
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # the specific node is val

        # 2. delete the key aka need to fill that node with another value that fulfils the BST 
        # like, maybe smallest of the right children or largest of the left? 
        # inorder successor vs predecessor, went with former here
        
        # case 1: no children, just delete
        # case 2: 1 child, just connect parent to that child and return child? 
            if not root.left:
                return root.right
            if not root.right:
                return root.left

        # case 3: 2 children
            updated_refer = self.getSuccessor(root)
            root.val = updated_refer.val # replace target node with that updated value
            root.right = self.deleteNode(root.right, updated_refer.val) # narrow down to case 1/2 now 
        
        return root
    
    def getSuccessor(self, node):
        node = node.right
        while node and node.left:
            node = node.left
        
        return node