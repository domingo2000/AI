from grid import Grid


def is_goal(self, square):
    """
    Defines if the given square state is a goal or not
    """
    if square.type == "goal":
        return True
    else:
        return False


def expand(self, grid, state):
    x, y = state
    return grid.neighbours(x, y)
