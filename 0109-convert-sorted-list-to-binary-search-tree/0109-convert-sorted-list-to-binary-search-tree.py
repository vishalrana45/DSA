# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if head == None:
            return None
        
        if head.next == None:
            return TreeNode(head.val)
        
        count = 0
        temp = head

        while temp != None:
            count += 1
            temp = temp.next
        
        mid = count // 2

        #divide the left and right node
        prev = None
        temp = head

        for i in range(mid):
            prev = temp
            temp = temp.next #temp stop at mid which is root
        
        root = TreeNode(temp.val)

        #Disconnect left half
        if prev:
            prev.next = None

        root.left = self.sortedListToBST(head) #left start from head
        root.right = self.sortedListToBST(temp.next) #temp is at mid(root) so next to root is right

        return root