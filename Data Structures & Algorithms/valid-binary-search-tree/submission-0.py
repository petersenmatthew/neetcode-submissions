# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower, upper):
            # pre-order 
            # node, left ,right
            if not node:
                return True
            # process node

            if not (lower < node.val < upper):
                return False
            # left node, is upper bounded by parent
            left_valid = dfs(node.left, lower, node.val)

            # right node, is lower bounded by parent
            right_valid = dfs(node.right, node.val , upper)

            if not left_valid or not right_valid:
                return False
            else:
                return True
        return dfs(root, float("-inf"), float("inf"))