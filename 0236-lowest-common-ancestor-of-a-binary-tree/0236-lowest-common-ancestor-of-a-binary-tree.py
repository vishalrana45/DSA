# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None] #ans[0] will store the Lowest Common Ancestor

        def fun(node, p ,q):
            if node == None:
                return 0

            left = fun(node.left, p, q)
            right = fun(node.right, p, q)

            current = 0
            if node == p or node == q:
                current += 1
            
            total = left + right + current

            if total == 2 and ans[0] == None:
                ans[0] = node

            return total

        fun(root, p, q) 
        return ans[0]
            
        