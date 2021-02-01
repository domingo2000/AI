from collections import deque
from PyQt5.QtCore import QObject, pyqtSignal


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


class SearchSolver(QObject):
    """
    Class with different algorithm to solve problems by search
    """
    senal_pintar_frontera = pyqtSignal(list)
    senal_pintar_recorrido = pyqtSignal(tuple)
    senal_pintar_solucion = pyqtSignal(deque)

    def __init__(self, initial_state, expand_f, is_goal):
        """
        The following functions must be passed for any given problem
        is_goal(state) -> bool
        expand_f(state) -> [states]
        """
        super().__init__()
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
        recorridos = deque()
        d.append(self.initial_state)
        COUNT = 0
        while len(d) > 0:
            COUNT += 1
            current_node = d.popleft()
            recorridos.append(current_node)

            if self.is_goal(current_node.state):
                solution = deque()
                while current_node.parent is not None:
                    solution.appendleft(current_node.state)
                    current_node = current_node.parent
                # ADS The root state to solution
                solution.appendleft(current_node.state)
                self.senal_pintar_solucion.emit(solution)
                return solution
            else:
                self.expand(current_node)
                d.extend(current_node.childs)
            if (COUNT % 10) == 0:
                print(f"Step: {COUNT}")

            self.senal_pintar_frontera.emit([node.state for node in d])
            self.senal_pintar_recorrido.emit(current_node.state)
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
        print("SOLVING...")
        if algorithm == "BFS":
            solution = self.BFS()
        elif algorithm == "DFS":
            solution = self.DFS()
        return solution
