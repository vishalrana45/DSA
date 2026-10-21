# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:

        def fun(root):
            if root == None:
                return
            
            root.left = fun(root.left)
            root.right = fun(root.right)

            if root.val == target:
                if root.left == None and root.right == None:
                    return None
            
            return root

        return fun(root)