# Maze Viewer Documentation

The Maze Viewer is a Python script that allows you to visualize a maze, represented by a text file, using the matplotlib library. The script can also display the solution to the maze, animate the process of finding the solution, and return the number of nodes to solve the maze in CLI mode.
Usage

To use the Maze Viewer, run the following command:

`./maze_viewer [OPTIONS] filepath`


## Arguments

    filepath - The path to the file with the maze map.


## Options

The Maze Viewer accepts the following options:

    -H, --help: Print a help message and exit.
    --animate: Animate the process of finding the solution to the maze.
    --color=COLOR: Set the color map for the maze. The color map should be a valid matplotlib color map. The default color map is 'gray'.
    --cli: Run the script in CLI mode. The script will return the number of nodes to solve the maze and 0 if it is unsolvable.


## Maze File Format

The Maze Viewer expects the maze map to be in a text file. The file should contain the following characters:

    *: Represents the path in the maze.
    X: Represents the walls in the maze.
    o: Represents the path of the solution in the maze.

Example:

```*X***X***X
*X*X*X*XXX
*X*X*X***X
*X*X*XXX*X
***X***X*X
*XXXXXXX*X
*X*******X
*X*XXXXXXX
*********X
XXXXXXXX**
```

This maze can be visualized with the following command:


`./maze_viewer path/to/maze.txt`

In this example, the script will use the default color map ('gray') to display the maze.


## CLI Mode

In CLI mode, the Maze Viewer will return the number of nodes to solve the maze and 0 if it is unsolvable. To run the script in CLI mode, use the --cli option:


`./maze_viewer --cli path/to/maze.txt`

If the maze is unsolvable, the script will return 0. If the maze is solvable, the script will return the number of nodes required to solve the maze.
Color Maps

The Maze Viewer supports different color maps for displaying the maze. The default color map is 'gray'. To set a different color map, use the --color=COLOR option, where COLOR is a valid matplotlib color map. You can find a list of valid color maps here: https://matplotlib.org/stable/tutorials/colors/colormaps.html#grayscale-conversion


## Animation

The Maze Viewer can animate the process of finding the solution to the maze. To animate the process, use the --animate option:

`./maze_viewer --animate path/to/maze.txt`

The animation will show each step of the process of finding the solution to the maze. Once the solution is found, the final solution will be displayed.

Note: Animating the process of finding the solution can take some time, depending on the complexity of the maze.