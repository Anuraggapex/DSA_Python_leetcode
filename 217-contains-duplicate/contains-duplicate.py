class Solution(object):
    def containsDuplicate(self, nums):
        hash=set()
        for n in nums:
            if n in hash:
                return True
            hash.add(n)
        return False 
        