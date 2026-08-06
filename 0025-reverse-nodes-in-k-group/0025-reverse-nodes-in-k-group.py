# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        left = head
        res = None
        prev_left = None
        size = k

        while True:
            right = left
            for i in range(size-1):
                if right == None:
                    break
                right = right.next

            if right:
                next_left = right.next
                prev = None
                curr = left

                for i in range(size):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt

                if prev_left:
                    prev_left.next = right
                prev_left = left

                if res == None:
                    res = right 
                left = next_left

            else:
                if prev_left:
                    prev_left.next = left
                if res == None:
                    res = left
                break

        return res

        
        
        