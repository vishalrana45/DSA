# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        def fun(root):
            if root == None:
                return 0

            if root.left == None and root.right == None:
                return 1
            
            left = fun(root.left)
            right = fun(root.right)

            # +1 because the current root is also part of the path
            if root.left == None:
                return 1 + right
            
            if root.right == None:
                return 1 + left
        
            return 1 + min(left, right)
        
        return fun(root)