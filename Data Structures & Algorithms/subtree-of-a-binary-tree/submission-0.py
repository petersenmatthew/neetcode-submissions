# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root1, root2):
            queue = deque([(root1, root2)])
            while queue:
                node1, node2 = queue.popleft()
                if node1 is None and node2 is None:
                    continue
                if node1 is None:
                    return False
                if node2 is None:
                    return False
                if node1.val != node2.val:
                    return False
                
                queue.append([node1.left, node2.left])
                queue.append([node1.right, node2.right])
            return True

        # traverse through main tree
        # if we hit a value that is the root of subroot, then we start checkign that subroot
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # check if isSubtree
            if isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False