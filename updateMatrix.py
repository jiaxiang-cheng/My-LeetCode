class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distance = []

        len_y = len(mat)
        len_x = len(mat[0])

        for i in range(len_y):
            distance.append([0] * len_x)
            # temp.append([0] * len_x)

        for y in range(len_y):
            for x in range(len_x):

                if mat[y][x] == 0:
                    distance[y][x] = 0
                else:
                    delta = 0
                    min_temp = 0

                    temp = []
                    for i in range(len_y):
                        # distance.append([0] * len_x)
                        temp.append([0] * len_x)

                    count = 0
                    count2 = 0

                    while count2 <= 2:
                        delta += 1

                        head_x = max(x - delta, 0)
                        tail_x = min(x + delta, len_x - 1)
                        head_y = max(y - delta, 0)
                        tail_y = min(y + delta, len_y - 1)

                        for m in range(head_x, tail_x + 1):
                            if mat[head_y][m] == 0:
                                temp[head_y][m] = abs(head_y - y) + abs(m - x)
                            if mat[tail_y][m] == 0:
                                temp[tail_y][m] = abs(tail_y - y) + abs(m - x)

                        for n in range(head_y, tail_y + 1):
                            if mat[n][head_x] == 0:
                                temp[n][head_x] = abs(head_x - x) + abs(n - y)
                            if mat[n][tail_x] == 0:
                                temp[n][tail_x] = abs(tail_x - x) + abs(n - y)

                        flag = 0
                        for i in range(len_y):
                            for j in range(len_x):
                                if temp[i][j] != 0 and flag == 0:
                                    min_temp = temp[i][j]
                                    flag = 1
                                if flag == 1 and temp[i][j] < min_temp and temp[i][j] != 0:
                                    min_temp = temp[i][j]

                        if min_temp != 0:
                            count = 1

                        if count == 1:
                            count2 += 1

                    distance[y][x] = min_temp
        return distance