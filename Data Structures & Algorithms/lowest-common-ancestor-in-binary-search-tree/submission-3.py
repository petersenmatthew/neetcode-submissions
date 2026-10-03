# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # ancestor has to be greater than one, and less than one
        # p.val < ancestor.val < q.val or q < ancestor < p

        LCA = None

        # traverse through tree, check that condition, and the find min()
        current = root
        while current:
            if p.val <= current.val <= q.val or q.val <= current.val <= p.val:
                 LCA = current
                 break
                
            if current.val > p.val and current.val > q.val:
                current = current.left
            else:
                current = current.right
        return LCA
            