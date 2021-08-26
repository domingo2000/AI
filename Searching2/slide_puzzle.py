import random
from searching import Problem, Solver
from copy import deepcopy
import parameters.parameters_slide_puzzle as p


class Game:
    """
    A Class that represent the slide puzzle game completly
    """
    def __init__(self, size, board=None):
        self.size = size
        self.pos_0 = None

        self.make_board(board)  # Makes the self.board attribute

        if not board:
            self.shuffle_board()

    def make_board(self, board=None):
        """
        Makes a list of lists representing the board of the game of size n x n
        and returns the board
        """
        # If you want to make a specific board for the game
        if board:
            self.board = board
            self.update_pos_0()
            return board

        board = []
        c = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(c)
                c += 1
            board.append(row)
        board[self.size - 1][self.size - 1] = 0
        self.board = board
        self.update_pos_0()
        return board

    def shuffle_board(self):
        for i in range(p.shuffling_number):
            directions = self.possible_directions()
            direction = random.choice(directions)
            self.move(direction)

    def print_board(self):
        """
        prints the board
        """
        format_space_size = 4
        print("-" * ((self.size + 2) * format_space_size))
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                number = self.board[i][j]
                row += f"|{number:^#{format_space_size}}"

            row += "|"
            print(row)
            print("-" * ((self.size + 2) * format_space_size))

    def print2_board(self, board=None):
        """
        prints the board
        """
        if not board:
            board = self.board
        format_space_size = 4
        print("-" * ((self.size) * format_space_size + 2))
        for i in range(self.size):
            row = "| "
            for j in range(self.size):
                number = board[i][j]
                row += f"{number:^#{format_space_size}}"

            row += "|"
            print(row)
        print("-" * ((self.size) * format_space_size + 2))

    def possible_directions(self):
        """
        See the position of the 0 piece and return the posible
        direcctions that you can play in a set of the form
        ["direction1", "direction2", ...]
        """
        max_index = self.size - 1
        # LeftTop Corner
        if self.pos_0 == [0, 0]:
            actions = ["RIGHT", "DOWN"]
        # RightTop Corner
        elif self.pos_0 == [0, max_index]:
            actions = ["LEFT", "DOWN"]
        # LeftBottom Corner
        elif self.pos_0 == [max_index, 0]:
            actions = ["RIGHT", "UP"]
        # RightBottom Corner
        elif self.pos_0 == [max_index, max_index]:
            actions = ["LEFT", "UP"]
        # LeftSide
        elif self.pos_0[1] == 0:
            actions = ["RIGHT", "UP", "DOWN"]
        # RightSide
        elif self.pos_0[1] == (max_index):
            actions = ["LEFT", "UP", "DOWN"]
        # TopSide
        elif self.pos_0[0] == 0:
            actions = ["LEFT", "RIGHT", "DOWN"]
        # BottomSide
        elif self.pos_0[0] == (max_index):
            actions = ["LEFT", "RIGHT", "UP"]
        else:
            actions = ["LEFT", "RIGHT", "UP", "DOWN"]

        return actions

    def move(self, direction):
        """
        Updates the board given the action (direcction)
        Direction keys = ["UP", "DOWN", "LEFT", "RIGHT"]
        """

        # Get the position of the 0
        i = self.pos_0[0]
        j = self.pos_0[1]

        if direction == "UP":
            new_i = i - 1
            new_j = j
        elif direction == "DOWN":
            new_i = i + 1
            new_j = j
        elif direction == "LEFT":
            new_i = i
            new_j = j - 1
        elif direction == "RIGHT":
            new_i = i
            new_j = j + 1
        else:
            raise ValueError("This is not a correct direction")

        # Gets the value of the neighbour
        value = self.board[new_i][new_j]

        # Swaps the value with the 0
        self.board[i][j] = value
        self.board[new_i][new_j] = 0

        # Update the value of the 0 position
        self.pos_0 = [new_i, new_j]

    def update_pos_0(self):
        """
        Search for the position of the value 0 and
        updates the self.pos_0 value of the instance
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    self.pos_0 = [i, j]

    def completed(self):
        """
        See if the puzzle numbers are correct and returns True if it is, False
        otherwise.
        """
        correct_numbers = [i for i in range(1, self.size**2)]
        correct_numbers.append(0)
        numbers = []
        for i in range(self.size):
            for j in range(self.size):
                number = self.board[i][j]
                numbers.append(number)
        if numbers == correct_numbers:
            return True
        else:
            return False

    def play(self):
        self.print2_board()
        while not self.completed():
            move = input("Enter a posible move (\"exit\" to exit): ").upper()

            if move == "EXIT":
                print("Byee!")
                break

            while move not in self.possible_directions():
                print("Invalid move!")
                move = input("Enter a posible move: ").upper()

            self.move(move)
            self.print2_board()

        print("Felicitaciones has ganado!")


class SlidePuzzleProblem(Problem):

    def __init__(self, game):
        # Extra attributes of this specific problem
        self.game = game

        # Initialzie the problem with the initial state and goal
        initial_state = deepcopy(game.board)
        goal = self.make_goal()
        super().__init__(initial_state, goal)

    def make_goal(self):
        # Makes the goal board (state) for the 8puzzle game
        goal = []
        c = 1
        for i in range(game.size):
            row = []
            for j in range(game.size):
                row.append(c)
                c += 1
            goal.append(row)
        goal[game.size - 1][game.size - 1] = 0

        return goal

    def actions(self, state):
        """
        See the position of the 0 piece in the state and return the posible
        direcctions that you can play in a set of the form
        {"direction1", "direction2", ...}
        """
        # Search for the position of 0 piece in puzzle
        for i in range(self.game.size):
            for j in range(self.game.size):
                if state[i][j] == 0:
                    pos_0 = [i, j]

        max_index = self.game.size - 1
        # LeftTop Corner
        if pos_0 == [0, 0]:
            actions = {"RIGHT", "DOWN"}
        # RightTop Corner
        elif pos_0 == [0, max_index]:
            actions = {"LEFT", "DOWN"}
        # LeftBottom Corner
        elif pos_0 == [max_index, 0]:
            actions = {"RIGHT", "UP"}
        # RightBottom Corner
        elif pos_0 == [max_index, max_index]:
            actions = {"LEFT", "UP"}
        # LeftSide
        elif pos_0[1] == 0:
            actions = {"RIGHT", "UP", "DOWN"}
        # RightSide
        elif pos_0[1] == (max_index):
            actions = {"LEFT", "UP", "DOWN"}
        # TopSide
        elif pos_0[0] == 0:
            actions = {"LEFT", "RIGHT", "DOWN"}
        # BottomSide
        elif pos_0[0] == (max_index):
            actions = {"LEFT", "RIGHT", "UP"}
        else:
            actions = {"LEFT", "RIGHT", "UP", "DOWN"}

        return actions

    def result(self, board, direction):
        """
        Returns the next state given an state and an action.
        """
        game = Game(self.game.size, deepcopy(board))
        game.move(direction)
        new_state = game.board
        return new_state


def print_state(state):
    """
    prints the board
    """
    board = state
    n = p.board_size
    format_space_size = 4
    print("-" * ((n) * format_space_size + 2))
    for i in range(n):
        row = "| "
        for j in range(n):
            number = board[i][j]
            row += f"{number:^#{format_space_size}}"

        row += "|"
        print(row)
    print("-" * ((n) * format_space_size + 2))


if __name__ == "#__main__":
    import parameters as p
    game = Game(p.board_size)
    game.play()
    # game.board = [[1, 2, 3],  # 0
    #               [4, 5, 6],  # 1
    #               [7, 0, 8]]  # 2
    #

if __name__ == "__main__":
    from slide_puzzle import Game

    print("Comenzando Programa [ok]")

    game = Game(p.board_size)
    problem = SlidePuzzleProblem(game)
    solver = Solver()

    print("Initial State:")
    game.print2_board(problem.initial_state)

    print("Problem Goal:")
    game.print2_board(problem.goal)

    path = solver.generic_solve(problem, algorithm=p.ALGORITHM_SOLVER)

    print("############################################")
    print("############################################")
    print("############################################")
    for step in path:
        print("MOVE:", step[1])
        print_state(step[0])
        print("next----")

    print("Solution lenght:", len(path))
