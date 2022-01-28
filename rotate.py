# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        tail = nums[- k:]
        for i in range(-1, -n + k - 1, -1):
            nums[i] = nums[i - k]

        for i in range(k):
            nums[i] = tail[i]
