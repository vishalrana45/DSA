# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 == None and list2 == None:
            return None
        
        temp = ListNode() #cannot directly return res becoz of datatype problem
        current = temp
        res = []
        
        while list1 and list2:
            if list1.val <= list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next
            
        while list1:
            res.append(list1.val)
            list1 = list1.next
        
        while list2:
            res.append(list2.val)
            list2 = list2.next
        
        for value in res:
            current.next = ListNode(value)
            current = current.next
        
        return temp.next #as temp is initially None so next store actual value