class Solution:
    def longestCommonPrefix(self, strings):
        length_str = []
        for i, j in enumerate(strings):
            length_str.append(len(j))

        ref = strings[length_str.index(min(length_str))]
        strings.remove(ref)
        flag, pref = 0, ""

        for i, j in enumerate(ref):
            for m, n in enumerate(strings):
                if j == n[i]:
                    pass
                else:
                    flag = 1
            if flag == 0:
                pref += j
            else:
                break
        return pref
