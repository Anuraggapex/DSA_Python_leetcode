class Solution(object):
    def isPalindrome(self, head):
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        left, right = 0, len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
            
        return True