# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        
        #first get all left as we need complexity better than O(n)
        left_h = 0
        node = root
        while node:
            left_h += 1
            node = node.left
        
        #same then go to complete right
        right_h = 0
        node = root
        while node:
            right_h += 1
            node = node.right
        
        #if both left and right have equal elements then tree is perfect
        if left_h == right_h:
            return 2 ** left_h - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)