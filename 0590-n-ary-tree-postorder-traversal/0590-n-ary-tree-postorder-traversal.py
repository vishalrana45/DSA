"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def fun(root):
            if root == None:
                return

            for child in root.children:
                fun(child)
            
            res.append(root.val)
        
        fun(root)
        return res 