import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Maze:
    def __init__(self, maze, color):
        d = {"*": 0, "o":1, "X":2}
        self.maze = maze
        self.maze_mat = [[d[_] for _ in i] for i in maze]
        self.color = color

    def show(self):
        plt.imshow(self.maze_mat, cmap=self.color)
        plt.show()
