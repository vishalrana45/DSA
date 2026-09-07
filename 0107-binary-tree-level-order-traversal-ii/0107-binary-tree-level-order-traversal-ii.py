# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        q.append(root)

        result = []
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result.append(level)

        result.reverse()
        return result
        
        