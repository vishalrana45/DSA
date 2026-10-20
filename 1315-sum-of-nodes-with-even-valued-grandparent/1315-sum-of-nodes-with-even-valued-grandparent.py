# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        sum = 0
    
        def fun(root):
            nonlocal sum

            if root == None:
                return

            if root.val % 2 == 0:

                if root.left:
                    if root.left.left:
                        sum += root.left.left.val
                    if root.left.right:
                        sum += root.left.right.val
                    
                if root.right:
                    if root.right.right:
                        sum += root.right.right.val
                    if root.right.left:
                        sum += root.right.left.val
            
            fun(root.left)
            fun(root.right)

        fun(root)
        return sum