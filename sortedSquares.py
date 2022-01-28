# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ls, head, tail = [], 0, -1
        n = len(nums)

        while head - tail != n:
            if nums[head] < 0:
                neg = nums[head]
            else:
                neg = 0

            if nums[tail] > 0:
                pos = nums[tail]
            else:
                pos = 0

            if pos > - neg:
                win = pos
                tail -= 1
            else:
                win = neg
                head += 1

            ls.insert(0, win * win)

        ls.insert(0, nums[head] * nums[head])

        return ls
