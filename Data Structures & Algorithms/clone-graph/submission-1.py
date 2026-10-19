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
     copy = Node(node.val)
     root = copy
     
     queue = deque([(node, copy)])
     
     # hash map:
     # og node -> copy 
     copies = {
       node: copy
     }
     while queue:
       node, copy = queue.popleft()
       for neighbor in node.neighbors:
         if neighbor in copies:
           copy.neighbors.append(copies[neighbor])
         else:
           copy_neighbor = Node(neighbor.val)
           copy.neighbors.append(copy_neighbor)
           copies[neighbor] = copy_neighbor
           queue.append((neighbor, copy_neighbor))
       
     return root
       