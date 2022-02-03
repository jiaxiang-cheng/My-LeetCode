class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        area_list = []

        image_y = len(grid)
        image_x = len(grid[0])
        initial_x = [0] * image_x
        visit = []
        # initial_y, visit, current, neighbor, image = [], [], [], [], []

        for i in range(image_y):
            # initial_y.append(initial_x.copy())
            # current.append(initial_x.copy())
            visit.append(initial_x.copy())
            # neighbor.append(initial_x.copy())

        for p in range(image_y):
            for q in range(image_x):

                if grid[p][q] == 1 and visit[p][q] != 1:

                    # initial_x = [0] * image_x
                    current, neighbor, image = [], [], []

                    for i in range(image_y):
                        current.append(initial_x.copy())
                        image.append(initial_x.copy())
                        neighbor.append(initial_x.copy())

                    neighbor[p][q] = 1

                    while 1:
                        current = neighbor.copy()

                        neighbor_list = []

                        for i in range(image_y):
                            for j in range(image_x):
                                if current[i][j] == 1:
                                    if i - 1 >= 0:
                                        if visit[i - 1][j] != 1:
                                            neighbor_list.append([i - 1, j])
                                            visit[i - 1][j] = 1
                                    if i + 1 <= image_y - 1:
                                        if visit[i + 1][j] != 1:
                                            neighbor_list.append([i + 1, j])
                                            visit[i + 1][j] = 1
                                    if j - 1 >= 0:
                                        if visit[i][j - 1] != 1:
                                            neighbor_list.append([i, j - 1])
                                            visit[i][j - 1] = 1
                                    if j + 1 <= image_x - 1:
                                        if visit[i][j + 1] != 1:
                                            neighbor_list.append([i, j + 1])
                                            visit[i][j + 1] = 1

                        if neighbor_list == []:
                            area = 0
                            for i in image:
                                area += sum(i)
                            # area = sum(image)
                            break

                        neighbor = []

                        for i in range(image_y):
                            neighbor.append(initial_x.copy())

                        for i, j in enumerate(neighbor_list):
                            r = j[0]
                            c = j[1]
                            if grid[r][c] == 1:
                                image[r][c] = 1
                                neighbor[r][c] = 1

                    area_list.append(area)