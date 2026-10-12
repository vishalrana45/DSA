# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        res = root.val
        max_depth = -1
        
        def fun(root, depth):
            nonlocal res, max_depth
            if root == None:
                return
            
            if depth > max_depth:
                max_depth = depth
                res = root.val

            fun(root.left, depth + 1)
            fun(root.right, depth + 1)
        
        fun(root, 0)
        return res