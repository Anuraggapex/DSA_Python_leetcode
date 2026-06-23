class Solution(object):
    def moveZeroes(self, nums):
        move=0
        n=len(nums)

        for i in range (n):
            if nums[i]!=0:
                nums[move], nums[i] = nums[i], nums[move]
                move+=1

        