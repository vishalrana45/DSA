# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def fun(root):
            nonlocal total

            if root == None:
                return 
            
            fun(root.right) #visit the largest node first
            
            total += root.val
            root.val = total
    
            fun(root.left)

        fun(root)
        return root 