# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 1)])
        output = []
        # (node, level)
        # output [[(node, 1), (node, 1)],[(node, 2), (node, 2)]]
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            # check last level in result
            if len(output) > 0 and output[-1][-1][1] == level: # if it matches the level same list eelemtn
                output[-1].append((node, level))
            else: # make new
                output.append([(node, level)])
                
        result = []
        for tuple_list in output:
            sub_list = []
            for node_tuple in tuple_list:
                sub_list.append(node_tuple[0].val)
            result.append(sub_list)
        return result
