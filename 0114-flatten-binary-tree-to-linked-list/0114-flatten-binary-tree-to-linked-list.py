# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        prev = None #we start from reverse by using dfs

        def dfs(node):
            nonlocal prev
        
            if node == None:
                return None
            
            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev = node
        
        dfs(root)