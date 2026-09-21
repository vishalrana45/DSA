# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        q = deque()
        q.append(root)

        nullfound = False

        while q:
            node = q.popleft()

            if node == None:
                nullfound = True
                continue

            if nullfound: #here nullfound is still false
                return False
            
            q.append(node.left)
            q.append(node.right)

        return True