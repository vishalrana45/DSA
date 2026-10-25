# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if root == None:
            return
        
        q = deque([root])
        level = 0

        while q:
            nodes = []

            for i in range(len(q)):
                node = q.popleft()
                nodes.append(node)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            if level % 2 == 1:
                left, right = 0, len(nodes) - 1

                while left < right:
                    nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
                
                    left += 1
                    right -= 1

            level += 1 
                
        return root if level else None