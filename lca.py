# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, n1, n2):
        if not root:
            return None

        # if either key matches with root, return root
        if root == n1 or root == n2:
            return root

        leftLca = self.lowestCommonAncestor(root.left, n1, n2)
        rightLca = self.lowestCommonAncestor(root.right, n1, n2)

        # if both non-null, it's the case where one is left and one is right
        if leftLca and rightLca:
            return root

        # check if left vs right subtree is lca
        return leftLca if leftLca else rightLca

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
        
#         # oh there's like different cases
#         # 1. p on left and q on right
#         # 2. both along the same path, so either p or q being the lowest node? or just propagate down? 
#         # ok so yea, current node being p or q, left contains vs right contains, fulfil 2 of these to be lca

#         def dfs(node, p, q): # outputs a bool or whether fulfils the cases
#             global lca
#             if not node:
#                 return False 

#             # checking whether each node fulfils
#             cur_node_p_or_q = node == p or node == q

#             left_contains = dfs(node.left, p, q)
#             right_contains = dfs(node.right, p, q)

#             if cur_node_p_or_q + left_contains + right_contains == 2:
#                 lca = node
            
#             # *
#             return (cur_node_p_or_q or left_contains or right_contains) 
        
#         dfs(root, p, q)
#         return lca
#         # checking each node is O(N^2) time and O(H) space

# # Worse runtime but better memory
# class Solution(object):
#     def lowestCommonAncestor(self, root, n1, n2):
#         path1 = []
#         path2 = []

#         # paths from root to n1 and root to n2
#         if not self.findPath(root, path1, n1) or not self.findPath(root, path2, n2):
#             return None

#         # compare paths for first different value
#         i = 0
#         while i < len(path1) and i < len(path2):
#             if path1[i] != path2[i]:
#                 return path1[i - 1]
#             i += 1

#         return path1[i - 1]

#     def findPath(self, root, path, n):
#         if root is None:
#             return False

#         # current node
#         path.append(root)

#         if root == n or self.findPath(root.left, path, n) or self.findPath(root.right, path, n):
#             return True

#         # remove root from path and return false
#         path.pop()
#         return False