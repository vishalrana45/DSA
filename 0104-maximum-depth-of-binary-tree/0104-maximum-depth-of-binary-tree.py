# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        def fun(root):
            if root == None:
                return 0
            
            left = fun(root.left)
            right = fun(root.right)

            return 1 + max(left, right)

        return fun(root)