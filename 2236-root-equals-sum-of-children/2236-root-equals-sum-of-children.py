# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:

        def fun(root):
            if root == None:
                return True

            if root.left == None and root.right == None:
                return True

            if root.left == None or root.right == None:
                return False
            
            if root.val != root.left.val + root.right.val:
                return False

            return fun(root.left) and fun(root.right)

        return fun(root)