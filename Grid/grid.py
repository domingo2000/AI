

class Grid:
    """
    Defines a Grid class of m x n squares, it can contains walls
    """

    def __init__(self, m, n):
        """
        m: height/rows
        n: width/columns
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

    def change_type(self, type, i, j):
        self.grid[i][j] = type


if __name__ == "__main__":
    map = Grid(4, 8)
    map.show()
    walls_coordinates = [(0, 0), (1, 1), (0, 1)]
    map.add_walls(walls_coordinates)
    map.show()
