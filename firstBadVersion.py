# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1) == True:
            return 1
        head, tail = 1, n
        while (tail - head) != 1:
            if isBadVersion(int((tail+head)/2)) == False:
                head = int((tail+head)/2)
            else:
                tail = int((tail+head)/2)
        return tail
