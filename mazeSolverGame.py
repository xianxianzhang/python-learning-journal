import  os

def display_maze(maze):
    """
    Display Maze in 2D Matrix format for Visualization.
    Parameters:
        maze (list): 2D list of ints where 1 represents a wall and 0 represents a valid path.

    Return:
        No Return

    """
    temp = maze[:]
    os.system('clear')

    draw = ""
    for row in temp:
        for item in row:
            item = str(item).replace("1",str(1)+'   ')
            item = str(item).replace("0", str(0)+'   ')

            draw += item
        draw += "\n"
    print(draw)


def solve_maze(maze, x, y, path):
    """
    Recursively find a path from the current position (x, y) to the exit in the maze.
    
    Parameters:
    maze (list): 2D list of ints where 1 represents a wall and 0 represents a valid path.
    x (int): Current row position in the maze.
    y (int): Current column position in the maze.
    path (list): A list of tuples representing the path taken.

    Returns:
    bool: True if a path exists, False otherwise.
    """
    # Check if current position is out of bounds or is a wall
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
        return False

    # Check if the current position is the exit (bottom-right corner)
    if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
        path.append((x, y))
        return True

    # Mark the current cell as visited (to avoid revisiting)
    maze[x][y] = 2
    path.append((x, y))

    # Recursively explore neighbors: down, right, up, left
    if (solve_maze(maze, x + 1, y, path) or  # Move down
        solve_maze(maze, x, y + 1, path) or  # Move right
        solve_maze(maze, x - 1, y, path) or  # Move up
        solve_maze(maze, x, y - 1, path)):   # Move left
        return True

    # Backtrack: Unmark the current cell and remove it from the path
    path.pop()
    maze[x][y] = 0
    return False


def find_maze_path(maze):
    """
    Wrapper function to start the maze solving process and return the path if one exists.

    Parameters:
    maze (list): 2D list of ints representing the maze.

    Returns:
    list: List of tuples representing the path if one exists, otherwise None.
    """
    path = []
    if solve_maze(maze, 0, 0, path):
        return path
    else:
        return None


# Sample maze: 0 represents a path, 1 represents a wall.
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]
display_maze(maze)
# Finding the path from start to end
path = find_maze_path(maze)

# Display the result
if path:
    print("Path found:", path)
else:
    print("No path found.")