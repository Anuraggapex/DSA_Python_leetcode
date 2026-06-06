class Solution(object):
    def isPalindrome(self, s):
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i.lower()     
        left = 0
        right = len(s1) - 1        
        while left < right:
            if s1[left]!=s1[right]:
                return False 
            left += 1
            right -= 1           
        return True
