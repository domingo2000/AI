

class Grid:
    """
    Defines a Grid class of m x n squares, it can contains walls
    """

    def __init__(self, m, n):
        """
        m: height/rows/y/i
        n: width/columns/x/j
        """
        self.rows, self.columns = m, n
        self.grid = [["normal" for j in range(n)] for i in range(m)]

    def show(self):
        """
        Displays the grid in the console
        """
        print(" ", "-" * self.columns * 2)
        for row in self.grid:
            string = "| "
            for square in row:
                string += square + " "
            print(string, "|")
        print(" ", "-" * self.columns * 2)

    def add_walls(self, coordinates):
        """
        Recive a list of coordinates of the form [(i,j), (i2, j2) ...]
        and adds the walls to that coordinates to the grid
        """
        for coordinate in coordinates:
            i, j = coordinate
            self.grid[i][j] = "wall"

    def change_type(self, type, x, y):
        self.grid[x][y] = type
        if type == "start":
            self.start = (x, y)
        elif type == "goal":
            self.goal = (x, y)
            print("goal coordinates:", x, y)

    def neighbours(self, coordinates):
        """
        Gives the coordinates of the neighbour cells that are expandable (not walls etc)
        Coorinates (x, y) are measured from the topleft corner
        """
        x, y = coordinates
        #  4 Corners
        if x == 0 and y == 0:  # Topleft Corner
            squares = [(x, y + 1), (x + 1, y)]
        elif x == 0 and y == (self.rows - 1):  # botom_left Corner
            squares = [(x, y - 1), (x + 1, y)]
        elif x == (self.columns - 1) and y == 0:  # Topright Corner
            squares = [(x, y + 1), (x - 1, y)]
        elif x == (self.columns - 1) and y == (self.rows - 1):  # BotommRight Corner
            squares = [(x, y - 1), (x - 1, y)]
        #  4 Sides
        elif x == 0:  # LeftSide square
            squares = [(x, y + 1), (x, y - 1), (x + 1, y)]
        elif x == (self.columns - 1):  # Rightside square
            squares = [(x, y + 1), (x, y - 1), (x - 1, y)]
        elif y == 0:  # Top square
            squares = [(x, y + 1), (x + 1, y), (x - 1, y)]
        elif y == (self.rows - 1):  # Bottom square
            squares = [(x, y - 1), (x + 1, y), (x - 1, y)]
        else:  # 4 Neighbour square
            squares = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        return squares

    def is_goal(self, coordinates):
        if self.goal == coordinates:
            return True
        else:
            return False


if __name__ == "__main__":
    map = Grid(4, 8)
    map.show()
    walls_coordinates = [(0, 0), (1, 1), (0, 1)]
    map.add_walls(walls_coordinates)
    map.show()
