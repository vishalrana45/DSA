# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left == None and right == None:
                return True
            
            if left == None or right == None:
                return False
            
            if left.val != right.val:
                return False
            
            return check(left.left, right.left) and check(left.right, right.right)
        
        if root == None:
            return False
        
        if subRoot == None:
            return true
        
        if check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


        
        