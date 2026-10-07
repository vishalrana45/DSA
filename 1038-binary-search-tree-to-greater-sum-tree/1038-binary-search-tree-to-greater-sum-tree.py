# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        sum = 0

        def fun(root):
            nonlocal sum
            if root == None:
                return 
            
            fun(root.right)
            sum += root.val
            root.val = sum
        
            fun(root.left)
        
        fun(root)
        return root