class Solution(object):
    def pivotIndex(self, nums):
        s=sum(nums)
        l=0
        r=s

        for i in range(len(nums)):
            r-=nums[i]

            if l==r:
                return i
            l+=nums[i]

        return-1



        

        
        