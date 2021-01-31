from collections import deque


class Node:
    id = 0

    def __init__(self, state, parent=None, childs=None):
        self.id = Node.id
        self.state = state
        self.parent = parent
        self.childs = childs
        Node.id += 1
    
    def __repr__(self):
        if self.parent == None:
            return f"Node: State = {self.state}, Parent = {self.parent}"
        else:
            return f"Node: State = {self.state}, Parent = {self.parent.id}"


class SearchSolver:
    """
    Class with different algorithm to solve problems by search
    """
    def __init__(self, initial_state, expand_f, is_goal):
        """
        The following functions must be passed for any given problem
        is_goal(state) -> bool
        expand_f(state) -> [states]
        """
        self.initial_state = Node(initial_state)
        # Functions used for algorithms
        self.is_goal = is_goal
        self.expand_f = expand_f

    def expand(self, node):
        node.childs = [Node(state, node) for state in self.expand_f(node.state)]

    def BFS(self):
        """
        Finds a solution by BFS search, returns a solution or False if failure.
        """
        d = deque()  # FIFO Structure for algorithm
        d.append(self.initial_state)
        COUNT = 0
        while len(d) > 0:
            COUNT += 1
            current_node = d.popleft()
            if self.is_goal(current_node.state):
                solution = deque()
                while current_node.parent is not None:
                    solution.appendleft(current_node.state)
                    current_node = current_node.parent
                # ADS The root state to solution
                solution.appendleft(current_node.state)
                return solution
            else:
                self.expand(current_node)
                d.extend(current_node.childs)
            if (COUNT % 1000) == 0:
                print(f"Step: {COUNT}")
        return False

    def DFS(self):
        """
        Finds a solution by BFS search, returns a solution or False if failure.
        """
        d = deque()  # FIFO Structure for algorithm
        d.append(self.initial_state)
        COUNT = 0
        while len(d) > 0:
            COUNT += 1
            current_node = d.pop()
            if self.is_goal(current_node.state):
                solution = deque()
                while current_node.parent is not None:
                    solution.appendleft(current_node.state)
                    current_node = current_node.parent
                # ADS The root state to solution
                solution.appendleft(current_node.state)
                return solution
            else:
                self.expand(current_node)
                d.extend(current_node.childs)
            if (COUNT % 100000) == 0:
                print(f"Step: {COUNT}")
        return False

    def a_star(self, heuristic):
        """
        Finds a solution using informed search with a given heuristic
        """
        # Terminar algoritmo
        nodes = {}
        h = heuristic()

    def solve(self, algorithm):
        if algorithm == "BFS":
            solution = self.BFS()
        elif algorithm == "DFS":
            solution = self.DFS()
        return solution
