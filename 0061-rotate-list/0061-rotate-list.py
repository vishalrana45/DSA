# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        last = head #let
        n = 1
        while last.next != None: #to find n and last(n-k th  element)
            n += 1
            last = last.next #to move last forward like n

        k = k % n
        if k == 0:
            return head
        
        t = head #(n-k)
        count = 1
        while t != None:
            if count == n-k:
                break
            t = t.next
            count += 1
        
        last.next = head
        res = t.next
        t.next = None #to point last node to null
        
        return res
        





        