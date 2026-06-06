class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
