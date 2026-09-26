# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ## edge case: 1 node:
        if head.next is None and n == 1:
            return None

        # dont have a tail
        # dont know lengtho f list

        # iterate through, find how long the list is
        # nth last node is (length + 1) - n
        length = 0
        cur = head

        while cur:
            length +=1
            cur = cur.next

        position = (length + 1) - n
        print(position)

        dummy = ListNode(0, head)
        cur = dummy

        # get to the node before that node to be removed
        for _ in range(position - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return dummy.next