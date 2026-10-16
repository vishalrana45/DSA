# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:

        def fun(root, val):
            if root == None:
                return True
            
            if root.val != val:
                return False
            
            return fun(root.left, val) and fun(root.right, val)
        
        return fun(root, root.val)