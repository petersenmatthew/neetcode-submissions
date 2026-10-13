# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur_node = root
        while cur_node:
            # check if its the LCA
            if p.val <= cur_node.val <= q.val or q.val <= cur_node.val <= p.val:
                return cur_node
            elif cur_node.val <= p.val and cur_node.val <= q.val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

        return root