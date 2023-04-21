import sys

import matplotlib.pyplot as plt
from matplotlib import animation

class Maze:
    def __init__(self, maze, color):
        self.transform =  {"*":2, "o":1, "X":0}
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
        self.maze_mat = [[self.transform[_] for _ in i] for i in maze]
        self.maze_res = [['*' if _ == 'o' else _ for _ in i] for i in maze]
        self.maze_res_mat = [[self.transform[_] for _ in i] for i in self.maze_res]
        self.color = color
        self.solve = self.__to_solve()
        self.im = None
        self.ax = None
        self.speed = 100

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
        return pos[0]

    def __to_solve(self, x_start=0, y_start=0):
        pos = [(x_start, y_start)]
        if sum(1 for i in "".join("".join(i) for i in self.maze) if i == 'o') == 0:
            return False
        if self.maze[0][0] != 'o':
            return False
        if self.maze[self.height - 1][self.width - 1] != 'o':
            return False
        is_available = True
        while is_available:
            tmp_pos = self.__next_posibility(pos[-1][0], pos[-1][1], pos)
            if not tmp_pos:
                is_available = False
            else:
                pos.append(tmp_pos)
        return pos


    def __animate_step(self, framenum):
        if self.solve:
            x, y = self.solve.pop(0)
            self.maze_res_mat[y][x] = 1
            im = self.ax.imshow(self.maze_res_mat, cmap=self.color)
            return im,
        else:
            im = self.ax.imshow(self.maze_res_mat, cmap=self.color)
            return im,

    def animate(self, speed : float):
        fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.maze_res_mat, cmap=self.color)

        if not self.solve:
            print("Map is not resolved", file=sys.stderr)
            return 1
        ani = animation.FuncAnimation(fig, self.__animate_step, frames=range(5), interval=speed, blit=True)
        plt.show()



