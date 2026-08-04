# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # keep track of the greatest value in a specific path, and every node should be greater than it to be considered good? 
        # also if encounter a not good node, all nodes from that node is also non good? 

        # count = 0
        # self.dfs(root, count, root.val)
        # return count

        # * this way to keep track of counts
        self.count = 0
        self.dfs(root, root.val)
        return self.count 
    
    # def dfs(self, node, count, max_val):
    def dfs(self, node, max_val): 
        # want to update count along the way
        if not node:
            return
        
        # if node.val < max_val:
        #     continue # <- also doesn't quite work in this case
        # else:
        #     count += 1 # might not work b/c local var? 
        #     # then dfs with node.val as max_val? 
        #     if node.left:
        #         self.dfs(node.left, count, node.val)
        #     if node.right: 
        #         self.dfs(node.right, count, node.val)

        # * focus on incrementing instead
        if node.val >= max_val: 
            self.count += 1
            max_val = node.val
        
        # * just directly do both b/c if no node.left or right it's just gonna return
        self.dfs(node.left, max_val)
        self.dfs(node.right, max_val)
        
        # time complexity of O(N) and space complexity O(H), height of tree, worst case O(N), O(log N) if balanced