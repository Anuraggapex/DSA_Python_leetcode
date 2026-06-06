class Solution(object):
    def reverse(self, x):
        s = -1 if x < 0 else 1
        r = int(str(abs(x))[::-1]) * s
        return r if -2147483648 <= r <= 2147483647 else 0