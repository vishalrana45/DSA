# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def fun(root, sum):
            if root == None:
                return False
            
            sum = sum + root.val

            #if root == leaf
            if root.left == None and root.right == None:
                if sum == targetSum:
                    return True
                else:
                    return False
            
            #if root == non-leaf
            return fun(root.left, sum) or fun(root.right, sum)

        return fun(root, 0)
        