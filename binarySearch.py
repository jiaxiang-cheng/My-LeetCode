# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums, target):
        i = 0
        n = len(nums)
        while nums[i] < target:
            i += 1
            if i == n:
                return -1
        if nums[i] == target:
            flag = i
        else:
            flag = -1
        return flag
