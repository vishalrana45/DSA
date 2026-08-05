# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = 1 #tell that where we are now and when to start to reverse
        temp = head
        before = None

        while pos < left: #mtbl abhi reverse nhi krna sirf abhi update krna hh temp ko jise before ko use kr ske prev pr point kene ke liye
            before  = temp
            temp = temp.next
            pos += 1

        curr = temp #agr condn satisfy nhi hoti toh before ke andr temp store ho jayega aur temp increase krega aur jb reverse ke condn aaygi toh automat. temp left pr aa jayega
        prev = None
        times = right-left+1
        
        while times:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            times -= 1
        
        temp.next = curr

        if before:
            before.next = prev
        else:
            head = prev

        return head

        
        




        