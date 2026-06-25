class Solution(object):
    def findMaxAverage(self, nums, k):
        win_sum=sum(nums[:k])
        max_sum=win_sum

        for i in range (k,len(nums)):
            win_sum=win_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum,win_sum)

        return float(max_sum)/k