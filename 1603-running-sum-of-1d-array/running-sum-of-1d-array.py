class Solution(object):
    def runningSum(self, nums):
        if len(nums)==0:
            return []
        psa=[0]*len(nums)
        psa[0]=nums[0]

        for i in range(1,len(nums)):
            psa[i]=nums[i]+psa[i-1]
        return psa
        