import os
import sys

# Increase recursion limit to handle larger mazes
sys.setrecursionlimit(2000)

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
            item = str(item).replace("1", str(1) + '   ')
            item = str(item).replace("0", str(0) + '   ')
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
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] != 0:
        return False

    if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
        path.append((x, y))
        return True

    maze[x][y] = 2
    path.append((x, y))

    if (solve_maze(maze, x + 1, y, path) or  # Move down
        solve_maze(maze, x, y + 1, path) or  # Move right
        solve_maze(maze, x - 1, y, path) or  # Move up
        solve_maze(maze, x, y - 1, path)):   # Move left
        return True

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

def run_test_cases():
    """
    Function to run and display results for various test cases of the maze solver.
    It uses the display_maze and find_maze_path functions to solve and visualize different mazes.
    """
    test_cases = [
        # Test Case 1: Basic Test Case
        [
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 0, 0]
        ],

        # Test Case 2: Fully Blocked Maze
         [
             [0, 1, 1],
             [0, 1, 1],
             [0, 1, 0]
         ],

        # # Test Case 3: No Walls (All Open)
         [
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
         ],

        # # Test Case 4: Edge Case (1x1)
         [
             [0]
         ],

        # # Test Case 5: Large Maze (10x10)
         [
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
             [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
             [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
         ],

        # # Test Case 6: Multiple Paths
         [
             [0, 0, 0, 1],
             [1, 1, 0, 1],
             [0, 0, 0, 0],
             [1, 1, 1, 0]
         ],

        # # Test Case 7: Corner Case: Exit Surrounded by Walls
         [
             [0, 0, 1, 1, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 0, 0]
         ],

        # # Test Case 8: Dead-End Maze
         [
             [0, 1, 1, 0],
             [0, 0, 1, 0],
             [1, 0, 1, 0],
             [0, 0, 0, 0]
         ],

        # # Test Case 9: Start Surrounded by Walls
         [
             [0, 1, 1],
             [1, 1, 1],
             [1, 1, 0]
         ],

        # # Test Case 10: Maze with Loops (Cyclic Paths)
         [
             [0, 1, 0, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 0],
             [0, 0, 0, 0, 0]
         ]
    ]

    for i, maze in enumerate(test_cases, start=1):
        print(f"\nTest Case {i}:")
        display_maze(maze)
        
        path = find_maze_path(maze)
        if path:
            print("Path found:", path)
        else:
            print("No path found.")

# Run all test cases
run_test_cases()