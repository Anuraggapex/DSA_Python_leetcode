# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        slow=head
        fast=head
        l=0

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            l+=1

        curr=head

        for i in range(l-1):
            curr=curr.next      
        curr.next=curr.next.next
        
        return head
        