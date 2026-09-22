''' Linked List Node Structure
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        curr = head
        count = 0

        while curr != None:
            count += 1
            curr = curr.next
        
        mid = count // 2
        curr = head
        
        for i in range(mid):
            curr = curr.next
        
        return curr.data

