class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        longest=0
        for nums in s:
            if nums-1 not in s:
                curr=1
                while nums+1 in s:
                    curr+=1
                    nums+=1
                longest=max(longest,curr)
        return longest
                