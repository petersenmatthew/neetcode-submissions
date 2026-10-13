# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 0)])
        output = []

        if not root:
            return []

        # nodes viewable on the right side are the LAST of 
        # their level to be processed in bfs traversal
        while queue:
            node, level = queue.popleft()
            if len(queue) == 0 or queue[0][1] != level:
                output.append(node.val)
            if node.left:
                queue.append((node.left, level + 1 ))
            if node.right:
                queue.append((node.right, level + 1))
        
        return output