# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        j = 1
        res = 1
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                j+=1
            else:
                i+=1
                res+=1
                j+=1
                current = current.next
        return head
        