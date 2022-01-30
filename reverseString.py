class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = int(len(s) / 2)

        for i in range(0, end):
            if s[i] == s[-(1 + i)]:
                continue
            else:
                temp = s[i]
                s[i] = s[-(1 + i)]
                s[-(1 + i)] = temp
