# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def fun(root):
            nonlocal res #tell the function to use outer res
            if root == None:
                return 0
            
            left = fun(root.left)
            right = fun(root.right)

            sum = left + right
            res = max(res, sum)

            return 1 + max(left, right)

        fun(root)
        return res
        