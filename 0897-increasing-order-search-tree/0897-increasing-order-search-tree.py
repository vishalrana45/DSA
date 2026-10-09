# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        ans = []

        def fun(root):
            nonlocal ans

            if root == None:
                return 
            
            fun(root.left)
            ans.append(root.val)
            fun(root.right)

        fun(root)
        
        dummy = TreeNode(0)
        curr = dummy

        for val in ans:
            curr.right = TreeNode(val)
            curr = curr.right
        
        return dummy.right #dummy.right points to the first actual node