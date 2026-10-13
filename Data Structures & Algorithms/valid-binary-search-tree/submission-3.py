# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # bfs?
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, lower, upper = queue.popleft()

            if not lower < node.val < upper:
                return False
            if node.left:
                queue.append((node.left, lower, node.val))
            
            if node.right:
                queue.append((node.right, node.val, upper))

        return True