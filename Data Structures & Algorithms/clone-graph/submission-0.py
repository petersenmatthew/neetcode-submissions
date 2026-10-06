"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root_copy = Node(node.val)

        queue = deque([node])
        copies = {
            node: root_copy
        }


        while queue:
            print(node.val)
            node = queue.popleft()
            node_copy = copies[node]
                

            for neighbor in node.neighbors:
                if neighbor not in copies:
                    neighbor_copy = Node(neighbor.val)
                    copies[neighbor] = neighbor_copy
                    queue.append(neighbor)
                
                node_copy.neighbors.append(copies[neighbor])

        return root_copy