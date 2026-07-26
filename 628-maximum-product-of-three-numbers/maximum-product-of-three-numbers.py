class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()

        s1=nums[-1]*nums[-2]*nums[-3]
        s2=nums[0]*nums[1]*nums[-1]
        
        return max(s1,s2)
        