# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
         
        dummy = ListNode(next = head)
        prev, curr = dummy, head #pointers

        while curr:  #have to keep going until curr becomes null

            nxt = curr.next  #what are we doing here ? {store}

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt #move to the next node

        return dummy.next #real head