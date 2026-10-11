# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        ans = []

        def fun(root, path):
            if root == None:
                return 
            
            path.append(str(root.val)) #add current node to path

            if root.left == None and root.right == None:
                ans.append("->".join(path))

            else:
                fun(root.left, path)
                fun(root.right, path)

            #backtracking
            path.pop()

        fun(root, [])
        return ans