# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []

        def fun(root, level):
            
            if root == None:
                return
            
            if level == len(ans):
                ans.append(root.val)

            fun(root.right, level + 1)  
            fun(root.left, level + 1)

        fun(root, 0)
        return ans 