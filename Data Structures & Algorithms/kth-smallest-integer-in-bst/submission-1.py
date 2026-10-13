# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return
            
            # go left
            left_result = dfs(node.left)

            if left_result is not None:
                return left_result

            # process current
            k-=1
            if k == 0:
                return node.val
            # go right


            right_result = dfs(node.right)

            if right_result is not None:
                return right_result

        return dfs(root)