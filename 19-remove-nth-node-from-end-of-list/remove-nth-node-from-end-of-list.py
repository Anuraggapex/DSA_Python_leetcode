class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        l=0
        while curr!=None:
            l += 1  
            curr = curr.next

        if l==n:
            return head.next
        
        curr=head

        for i in range(l-n-1):
            curr=curr.next      
        curr.next=curr.next.next
        
        return head