# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        if not subRoot:
            return True
        if not root:
            return False
        def check_same_dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            # check left & rught subtree if same
            return check_same_dfs(node1.left, node2.left) and check_same_dfs(node1.right, node2.right)

        queue = deque([root])
        isSubtree = False
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                isSubtree = check_same_dfs(node, subRoot)
                if isSubtree:
                    return True
    
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return isSubtree

