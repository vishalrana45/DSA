"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
    
        def fun(root):
            if root == None:
                return 0
            
            count = 0
           
            for child in root.children:
                count = max(count, fun(child))

            return count + 1

        return fun(root)