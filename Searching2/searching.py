from abc import ABC, abstractmethod
from copy import deepcopy
import parameters.parameters_search as p
from collections2 import Queue, Stack
from collections import deque


class Node:

    id = 0

    def __init__(self, parent, state, action) -> None:
        self.id = Node.id
        Node.id += 1
        self.parent = parent  # parent node of the node
        self.state = state  # State that describes the entire problem
        self.action = action  # The action of the parent that gets you to this node


class Problem(ABC):

    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    @abstractmethod
    def actions(self, state):
        """
        Returns a set of posible actions given a state of the problem.
        """
        pass

    @abstractmethod
    def result(self, state, action):
        """
        Returns the next state given an state and an action.
        """
        pass

    def goal_test(self, state):
        """
        Checks if a given state is the goal of the problem, returns a boolean
        """
        if state == self.goal:
            return True
        else:
            return False


class Solver:

    def __init__(self):
        self.path = None

    # @abstractmethod
    # def expand(self):
    #     pass

    def child_node(self, problem, parent, action) -> Node:
        """
        Makes a child node given the parent node for a given problem
        and returns the node
        """
        new_state = problem.result(parent.state, action)
        node = Node(parent, new_state, action)
        return node

    def is_goal(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def generic_solve(self, problem, algorithm="BFS"):
        """
        Search for a goal with bfs algorithm
        """
        if algorithm == "BFS":
            print("SOLVING BY BFS Algorithm")
            structure = Queue
        elif algorithm == "DFS":
            print("SOLVING BY DFS Algorithm")
            structure = Stack
        step = 0  # Counts the depth of the search in the algorithm
        node = Node(None, problem.initial_state, None)
        if problem.goal_test(node.state):
            return self.solution(node)  # It could return only the node, and then use solution

        frontier = structure()  # Changes the type of data-structure depending on the algorithm
        frontier.appendleft(node)
        explored = []  # Set with all the explored STATES of the problem

        while True:
            if len(frontier) == 0:  # If all states are explored and frontier is empty returns False
                return False
            node = frontier.pop()

            # Add the state, not the node because the graph have loops for states, not nodes
            explored.append(node.state)
            for action in problem.actions(node.state):  # Expands the node by the actions
                child = self.child_node(problem, node, action)
                if (child.state not in explored) and (child not in frontier):
                    if problem.goal_test(child.state):  # Checks the goal for the current childs
                        return self.solution(child)
                    frontier.append(child)

            # if (step % p.step_print) == 0:  # Show steps when reach some interval
            #     print("STEP=", step)
            if step >= p.max_step:  # Stops the searching at given step
                print("-----FRONTIER-------")
                print([(node.state) for node in frontier])
                print("-----EXPLORED-------")
                print(explored)
                break
            step += 1

    def bfs_solve(self, problem):
        """
        Search for a goal with bfs algorithm
        """
        step = 0  # Counts the depth of the search in the algorithm
        node = Node(None, problem.initial_state, None)
        if problem.goal_test(node.state):
            return self.solution(node)  # It could return only the node, and then use solution

        frontier = Queue()  # Deque or other FIFO Structure with nodes for BFS
        frontier.appendleft(node)
        explored = []  # Set with all the explored STATES of the problem

        while True:
            if len(frontier) == 0:  # If all states are explored and frontier is empty returns False
                return False
            node = frontier.pop()

            # Add the state, not the node because the graph have loops for states, not nodes
            explored.append(node.state)
            for action in problem.actions(node.state):  # Expands the node by the actions
                child = self.child_node(problem, node, action)
                if (child.state not in explored) or (child not in frontier):
                    if problem.goal_test(child.state):  # Checks the goal for the current childs
                        return self.solution(child)
                    frontier.append(child)

            if (step % p.step_print) == 0:  # Show steps when reach some interval
                print("STEP=", step)
            if step >= p.max_step:  # Stops the searching at given step
                break
            step += 1

    def solution(self, node):
        """
        Returns the solution path given a solution node
        """
        path = deque()
        step = (node.state, node.action)
        path.appendleft(step)

        while node.parent is not None:
            node = node.parent
            step = (node.state, node.action)
            path.appendleft(step)

        return path


if __name__ == "__main__":
    solver = Solver()
    node_1 = Node(None, "start", None)
    node_2 = Node(node_1, 2, "action 1")
    node_3 = Node(node_2, 2, "action 2")
    node_4 = Node(node_3, 2, "action 3")
    node_5 = Node(node_4, "goal", "action 4")
    print(solver.solution(node_5))
