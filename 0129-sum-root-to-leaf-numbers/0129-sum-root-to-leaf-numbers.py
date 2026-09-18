# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        def fun(root, sum):
            if root == None:
                return 0
            
            sum = sum * 10 + root.val

            if root.left == None and root.right == None:
                return sum

            return fun(root.left, sum) + fun(root.right, sum)
        
        return fun(root, 0)