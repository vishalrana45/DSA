class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack1 = []  # iterator for smallest elements
        stack2 = []  # iterator for largest elements

        # Push path to the smallest element
        def pushLeft(node):
            while node:
                stack1.append(node)
                node = node.left

        # Push path to the largest element
        def pushRight(node):
            while node:
                stack2.append(node)
                node = node.right

        pushLeft(root)
        pushRight(root)

        while stack1 and stack2:

            small = stack1[-1]
            big = stack2[-1]

            # Same node means both pointers have met
            if small == big:
                return False

            curr_sum = small.val + big.val

            if curr_sum == k:
                return True

            elif curr_sum < k:
                # Move the small pointer forward
                node = stack1.pop()

                if node.right:
                    pushLeft(node.right)

            else:
                # Move the big pointer backward
                node = stack2.pop()

                if node.left:
                    pushRight(node.left)

        return False
