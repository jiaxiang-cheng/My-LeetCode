class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        if s == "":
            return (0)
        if len(s) == 1:
            return (1)
        temp = s[0]
        flag = 0
        str_list = []
        len_list = []
        while index < len(s) - 1:
            index += 1
            for i, j in enumerate(temp):
                if s[index] == j:
                    flag = 1
                    break
            if flag == 1:
                str_list.append(temp)
                temp = s[index]
                flag = 0
            else:
                temp += s[index]

        for i, j in enumerate(str_list):
            len_list.append(len(j))

        return max(len_list)
