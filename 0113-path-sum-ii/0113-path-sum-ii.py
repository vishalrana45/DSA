# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []

        def fun(root, sum , diary): #dairy to maintain kon sa path add ho gya kon sa nhi
            if root == None:
                return None

            sum = sum + root.val
            diary = diary + [root.val] #pta chl jayega ki hum yha aaye hh

            if root.left == None and root.right == None:
                if sum == targetSum:
                    res.append(diary)
                return None

            fun(root.left, sum, diary)
            fun(root.right, sum, diary)
        
        fun(root, 0, [])
        return res



        