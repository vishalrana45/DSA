# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
            
        q = deque([root])
        res = []
        
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node is None:
                    res.append("#")
                    continue
                
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            
        return ",".join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans