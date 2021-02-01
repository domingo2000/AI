from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from collections import deque
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class GridWindow(QWidget):
    """
    Defines the main window of the program, that consist in the windows with the grid
    """

    #  Signals
    senal_cambiar_estilo = pyqtSignal(str, int, int)
    senal_llamar_vecinos = pyqtSignal(int, int)
    senal_resolver_camino = pyqtSignal(str)

    def __init__(self, m, n):
        super(GridWindow, self).__init__()
        uic.loadUi('grid_solver.ui', self)
        self.squares = {}
        self.init_grid(m, n)
        self.show()

    def init_grid(self, m, n):
        for i in range(m):
            for j in range(n):
                square = Square(self.grid_frame, x=j, y=i)
                self.squares[f"{j},{i}"] = square
                self.grid_frame.layout().addWidget(square, i, j)

    def solve_grid(self):
        self.senal_resolver_camino.emit(self.algorithm.currentText().upper())

    def paint_path(self, coordinate):
        x, y = coordinate
        self.squares[f"{x},{y}"].type = "path"

    def paint_frontier(self, coordinates):
        for coordinate in coordinates:
            x, y = coordinate
            self.squares[f"{x},{y}"].type = "frontier"

    def paint_solution(self, coordinates):
        for coordinate in coordinates:
            x, y = coordinate
            self.squares[f"{x},{y}"].type = "solution"


class Square(QLabel):
    """
    Defines each square of the grid, it can be swaped from normal, wall, start, goal
    """
    types = {"wall": "black", "goal": "green", "start": "red", "path": "yellow",
             "frontier": "purple", "solution": "blue", "normal": "white"}

    def __init__(self, parent, type="normal", x=None, y=None):
        super().__init__(parent)
        self.setMinimumHeight(5)
        self.setMinimumWidth(5)
        self.type = type
        self.type_deque = deque(self.types.keys())
        self.setStyleSheet(f"background-color: {self.types[type]}; border: 0px;")
        self.x = x
        self.y = y

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.setStyleSheet(f"background-color: {self.types[value]}; border: 0px;")
        self.parent().parent().senal_cambiar_estilo.emit(value, self.x, self.y)

    def mousePressEvent(self, event):
        self.type = self.type_deque.popleft()
        self.type_deque.append(self.type)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = GridWindow(4, 8)
    app.exec_()
