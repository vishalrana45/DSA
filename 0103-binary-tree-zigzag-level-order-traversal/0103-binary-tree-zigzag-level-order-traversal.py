# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        q = deque()
        q.append(root)
        level_num = 0

        result = []
        while q:
            level =  []

            for i in range(len(q)):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if level_num % 2 == 1:
                level.reverse()
            
            result.append(level)
            level_num += 1
        
        return result
        