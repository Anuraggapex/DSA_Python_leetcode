class Solution(object):
    def maxSubArray(self, nums):
        maxs=nums[0]
        curr=nums[0]

        for i in nums[1:]:
            if curr<0:
                curr=0

            curr+=i
            maxs=max(maxs,curr)

        return maxs

        