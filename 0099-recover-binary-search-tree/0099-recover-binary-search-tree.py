# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None 
        galat = 0
        first = None
        second = None

        def inorder(root):
            nonlocal prev, galat, first, second
            
            if root == None:
                return True

            if not inorder(root.left): #if left is invalid
                return False

            if prev == None:
                prev = root

            #Current node must be greater than previous node
            else:
                if root.val <= prev.val:
                    galat += 1

                    if galat == 1:
                        first = prev
                    
                    second = root
                
                prev = root

            #Check right subtree
            return inorder(root.right)

        inorder(root)
        first.val, second.val = second.val, first.val
        