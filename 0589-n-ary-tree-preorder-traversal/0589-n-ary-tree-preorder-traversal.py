"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def fun(root):
            if root == None:
                return
            
            res.append(root.val)

            for child in root.children:
                fun(child)

        fun(root)
        return res 