# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        
        def fun(root, key):
            if root == None:
                return None
            
            if key < root.val:
                root.left = fun(root.left, key)
            
            elif key > root.val:
                root.right = fun(root.right, key)
            
            else:
                if root.left == None:
                    return root.right
                
                elif root.right == None:
                    return root.left
                
                else:
                    temp = root.right

                    while temp.left:
                        temp = temp.left
                    
                    root.val = temp.val
                    root.right = fun(root.right, temp.val)
                
            return root
        
        return fun(root, key)