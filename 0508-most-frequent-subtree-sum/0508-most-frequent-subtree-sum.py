from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        freq = Counter()

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total = node.val + left_sum + right_sum

            freq[total] += 1

            return total

        dfs(root)

        max_freq = max(freq.values())

        return [s for s, count in freq.items() if count == max_freq]
