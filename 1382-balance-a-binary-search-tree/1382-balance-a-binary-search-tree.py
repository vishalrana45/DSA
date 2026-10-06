# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        ans = []
        def fun(root): 
            if root == None:
                return

            #inorder traversal to sort the array
            fun(root.left)
            ans.append(root.val)
            fun(root.right)
        
        fun(root)

        def build(l, r): #l and r is left and right resp.
            if l > r:
                return None
            
            mid = (l + r) // 2

            node = TreeNode(ans[mid])
            node.left = build(l , mid - 1)
            node.right = build(mid + 1 , r)
        
            return node
        return build(0, len(ans) - 1)