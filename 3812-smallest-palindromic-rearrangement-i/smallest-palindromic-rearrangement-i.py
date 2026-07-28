class Solution:
    def smallestPalindrome(self, s: str) -> str:
        return (t:=''.join(sorted(s[:(n:=len(s))//2])))+n%2*s[n//2]+t[::-1]