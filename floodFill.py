class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        current_color = image[sr][sc]
        image[sr][sc] = newColor

        image_y = len(image)
        image_x = len(image[0])
        initial_x = [0] * image_x
        initial_y, visit, current, neighbor = [], [], [], []

        for i in range(image_y):
            initial_y.append(initial_x.copy())
            current.append(initial_x.copy())
            visit.append(initial_x.copy())
            neighbor.append(initial_x.copy())

        neighbor[sr][sc] = 1

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
                break

            for i in range(image_y):
                neighbor.append(initial_x.copy())

            for i, j in enumerate(neighbor_list):
                r = j[0]
                c = j[1]
                if image[r][c] == current_color:
                    image[r][c] = newColor
                    neighbor[r][c] = 1

        return image