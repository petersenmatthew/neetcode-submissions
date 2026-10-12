# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # dfs solution iterative (pre-order)
        stack = [(root, 1)]
        # node, height
        depth = 0
        while stack:
            # process root
            node, height = stack.pop()
            depth = max(height, depth)
            # left
            if node.left:
                stack.append((node.left, height + 1))
            # right
            if node.right:
                stack.append((node.right, height + 1))
        return depth

            