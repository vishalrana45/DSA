# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0
        ans = 0

        def inorder(root):
            nonlocal count, ans
            
            if root == None:
                return None
            
            inorder(root.left)
            
            count += 1

            if count == k:
                ans = root.val
                return 

            inorder(root.right)

        inorder(root)
        
        return ans