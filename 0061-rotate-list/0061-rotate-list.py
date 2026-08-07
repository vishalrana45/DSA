# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        last = head #let head in starting, what is last element in node
        n = 1
        while last.next != None: #to find n and last element of node
            n += 1
            last = last.next #to move last forward like n

        k = k % n #to handle if k > n
        if k == 0:
            return head
        
        t = head #to find (n-k)
        count = 1
        while t != None:
            if count == n-k: #we can't use t here because of data type
                break
            t = t.next
            count += 1 
        
        last.next = head #to point last element before rotation with first element
        res = t.next #new head
        t.next = None #to point last node after rotation to null

        return res
        





        