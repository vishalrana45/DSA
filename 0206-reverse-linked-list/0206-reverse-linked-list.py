# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #before curr(head)
        curr = head
        while curr != None: #now simple swapping
            next = curr.next #save next node
            curr.next = prev #reverse the link
            prev = curr #move prev forward
            curr = next #move curr forward
        return prev #new head