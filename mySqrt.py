# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x):
        i = 0
        while x > i * i:
            i += 1
        return i - 1
