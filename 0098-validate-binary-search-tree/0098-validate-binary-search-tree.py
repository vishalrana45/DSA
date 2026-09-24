# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = None 

        def inorder(root):
            nonlocal prev

            if root == None:
                return True

            if not inorder(root.left): #if left is invalid
                return False

            if prev == None:
                prev = root

            #Current node must be greater than previous node
            else:
                if root.val <= prev.val:
                    return False

                prev = root

            #Check right subtree
            return inorder(root.right)

        return inorder(root)