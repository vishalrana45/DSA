# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        prev = None
        count = 0

        def fun(root):
            nonlocal prev, count
            if root == None:
                return 
            
            fun(root.left)
            
            if root.val == prev:
                count += 1
            else:
                count = 1
            
            prev = root.val

            fun(root.right)

        return count# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        prev = None
        count = 0
        max_count = 0
        ans = []

        def fun(root):
            nonlocal prev, count, max_count, ans
            if root == None:
                return 
            
            fun(root.left)
            
            if root.val == prev:
                count += 1
            else:
                count = 1
            
            prev = root.val

            if count > max_count:
                max_count = count
                ans = [root.val]
            elif count == max_count:
                ans.append(root.val)

            fun(root.right)

        fun(root)
        return ans