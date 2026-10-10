# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:

        ans1 = []
        def fun1(root1):
            nonlocal ans1

            if root1 == None:
                return 
            
            fun1(root1.left)
            ans1.append(root1.val)
            fun1(root1.right)
        
        fun1(root1)

        ans2 = []
        def fun2(root2):
            nonlocal ans2

            if root2 == None:
                return 
            
            fun2(root2.left)
            ans2.append(root2.val)
            fun2(root2.right)
        
        fun2(root2)

        res = ans1 + ans2
        res.sort()

        return res