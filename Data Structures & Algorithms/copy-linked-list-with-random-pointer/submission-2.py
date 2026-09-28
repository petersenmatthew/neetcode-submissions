"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # map to store what we alr have:
        # original node: copied ndoe

        known = {}

        cur = head

        while cur:
            new_node = Node(cur.val)
            known[cur] = new_node
            cur = cur.next
        
        for node in known:
            if node.next is not None:
                known[node].next = known[node.next]
            if node.random is not None:
                known[node].random = known[node.random]
        return known[head]