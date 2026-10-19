# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root == None:
            return []
        
        q = deque([root])
        ans = []

        while q:
            size = len(q)
            total = 0

            for i in range(size):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            ans.append(total/size)

        return ans        