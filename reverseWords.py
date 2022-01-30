class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        rs = ""
        for i, j in enumerate(s):
            if j != " ":
                word += j
            else:
                end = int(len(word) / 2)
                s = list(word)

                for k in range(0, end):
                    if s[k] == s[-(1 + k)]:
                        continue
                    else:
                        temp = s[k]
                        s[k] = s[-(1 + k)]
                        s[-(1 + k)] = temp
                rword = ''.join(s)
                if rs != "":
                    rs += " "
                    rs += rword
                else:
                    rs = rword

                word = ""

        end = int(len(word) / 2)
        s = list(word)

        for k in range(0, end):
            if s[k] == s[-(1 + k)]:
                continue
            else:
                temp = s[k]
                s[k] = s[-(1 + k)]
                s[-(1 + k)] = temp
        rword = ''.join(s)
        if rs != "":
            rs += " "
            rs += rword
        else:
            rs = rword

        return rs
