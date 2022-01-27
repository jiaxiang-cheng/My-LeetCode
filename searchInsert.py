# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        i = 0
        n = len(nums)
        while nums[i] < target:
            i += 1
            if i == n:
                break
        return i