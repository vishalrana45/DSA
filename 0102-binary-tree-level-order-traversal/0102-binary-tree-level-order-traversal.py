# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Using the deque..
        if root == None:
            return []

        q = deque()
        q.append(root)

        result = [] #to store all levels together
        while q:
            level = [] #to store each level sep.
            
            for i in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result.append(level)
        
        return result
        