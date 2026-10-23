# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:

        def fun(root):
            if root == None:
                return False
        
            if root.val == 2:
                return fun(root.left) or fun(root.right)
            
            if root.val == 3:
                return fun(root.left) and fun(root.right)

            if root.val == 0 or root.val == 1:
                return bool(root.val)
            
        return fun(root) 