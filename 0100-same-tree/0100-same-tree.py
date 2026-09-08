# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def fun(root1, root2):
            if root1 == None and root2 == None:
                return True
            
            if root1 == None or root2 == None:
                return False
            
            if root1.val != root2.val:
                return False
            
            r1 = fun(root1.left, root2.left)
            r2 = fun(root1.right, root2.right)

            if r1 and r2:
                return True
            else:
                return False
        
        return fun(p, q) #p and q are original trees
    
        