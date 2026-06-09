class Solution(object):
    def sortColors(self, nums):
        freq = [0] * 3
        for i in nums:
            freq[i] += 1
        new_lst = []
        for i in range(3):
            while freq[i] > 0:
                new_lst.append(i)
                freq[i] -= 1
        nums[:] = new_lst


