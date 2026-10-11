# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        sum = 0

        def fun(root):
            nonlocal sum
            if root == None:
                return
            
            if root.left != None:
                if root.left.left == None and root.left.right == None:
                    sum += root.left.val
                
            fun(root.left)
            fun(root.right)

        fun(root)
        return sum