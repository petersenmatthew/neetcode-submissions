# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # viewable: parent does not have right child (if left)
        # compare to others on its level

        # bfs where we store level
        # (node, level)
        # append right node first 
        # when we hit new level, first node is the one vieewable
        if not root:
            return []

        output = []
        queue = deque([(root, 1)])
        cur_lvl = 0
        while queue:
            node, level = queue.popleft()
            # (node, 2)
            if level != cur_lvl:
                output.append(node.val)
                cur_lvl += 1
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return output