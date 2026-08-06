# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        left = head
        res = None #that store the new head 
        prev_left = None #none because of first pair, use to connect external pair
        size = 2 #size = 2 because we need to deal with pair

        while True: #infinite loop because we don't know how values even or odd
            right = left #right = head
            for i in range(size-1): #to set right
                if right == None: #handle odd case
                    break
                right = right.next

            if right: #till right = None
                next_left = right.next #tell from where next pair start
                prev = None
                curr = left

                for i in range(size):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt

                if prev_left: #for connect external pair
                    prev_left.next = right #to connect the external pair
                prev_left = left

                if res == None: #to store new head
                    res = right 
                left = next_left

            else: #right is null, odd case
                if prev_left:
                    prev_left.next = left
                if res == None: #case if only one node present
                    res = left
                break

        return res

        