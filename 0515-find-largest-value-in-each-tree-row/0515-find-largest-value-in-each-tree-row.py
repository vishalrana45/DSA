# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        res = []

        def fun(root):
            nonlocal res

            if root is None:
                return 
            
            q = deque([root])
            
            while q:
                level_max = float('-inf')

                for i in range(len(q)):
                    node = q.popleft()

                    level_max = max(level_max, node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
                    
                res.append(level_max)

        fun(root)

        return res