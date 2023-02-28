import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Maze:
    def __init__(self, maze, color):
        d = {"*":0, "o":1, "X":2}
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
        self.maze_mat = [[d[_] for _ in i] for i in maze]
        self.maze_res = [['*' if _ == 'o' else _ for _ in i] for i in maze]
        self.color = color

    def show(self):
        plt.imshow(self.maze_mat, cmap=self.color)
        plt.show()

    def __is_coords_in_list(self, x:int, y:int, passed) -> bool:
        for i, j in passed:
            if i == x and j == y:
                return 1
        return 0

    def __next_posibility(self, x, y, passed=[]):
        pos = []
        if x > 0:
            if self.maze[y][x - 1] == 'o' and not self.__is_coords_in_list(x - 1, y, passed):
                pos.append((x - 1, y))
        if x < self.width - 1:
            if self.maze[y][x + 1] == 'o' and not self.__is_coords_in_list(x + 1, y, passed):
                pos.append((x + 1, y))
        if y > 0:
            if self.maze[y - 1][x] == 'o' and not self.__is_coords_in_list(x, y - 1, passed):
                pos.append((x, y - 1))
        if y < self.height - 1:
            if self.maze[y + 1][x] == 'o' and not self.__is_coords_in_list(x, y + 1, passed):
                pos.append((x, y + 1))
        if len(pos) != 1:
            return []
        return pos

    def __to_solve(self, x_start=0, y_start=0):
        d = {"*":0, "o":1, "X":2}
        pos = [(x_start, y_start)]

        if sum(1 for i in [_ for _ in self.maze] if i == 'o') == 0:
            return "Not path finding"
        if self.maze[0][0] != 'o':
            return "Don't start in 0 0"
        if self.maze[self.height - 1][self.width - 1] != 'o':
            return "Don't end in the right bottom corner"
        is_available = True
        while is_available:
            is_available = False


