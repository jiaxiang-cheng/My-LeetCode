class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        n_zero = 0
        i = 0
        while i < n - n_zero:
            if nums[i] == 0:
                n_zero += 1
                for j in range(i + 1, n):
                    nums[j - 1] = nums[j]
                nums[-1] = 0
            else:
                i += 1