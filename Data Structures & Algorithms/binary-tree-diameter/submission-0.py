# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # returns height
        def dfs(curr):
            if not curr:
                return 0
            # post-order (left, right, root)

            left = curr.left
            right = curr.right
            
            self.res = max(self.res, dfs(left) + dfs(right))
            return 1 + max(dfs(left), dfs(right))
        dfs(root)
        return self.res
