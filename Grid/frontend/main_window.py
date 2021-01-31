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

    def __init__(self, m, n):
        super(GridWindow, self).__init__()
        uic.loadUi('grid_solver.ui', self)
        self.init_grid(m, n)
        self.show()

    def init_grid(self, m, n):
        for i in range(m):
            for j in range(n):
                square = Square(self.grid_frame, x=i, y=j)
                self.grid_frame.layout().addWidget(square, i, j)


class Square(QLabel):
    """
    Defines each square of the grid, it can be swaped from normal, wall, start, goal
    """
    types = {"wall": "black", "goal": "green", "start": "red", "normal": "white"}

    def __init__(self, parent, type="normal", x=None, y=None):
        super().__init__(parent)
        self.type = type
        self.type_deque = deque(self.types.keys())
        self.setStyleSheet(f"background-color: {self.types[type]};")
        self.x = x
        self.y = y

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.setStyleSheet(f"background-color: {self.types[value]};")
        self.parent().parent().senal_cambiar_estilo.emit(value, self.x, self.y)

    def mousePressEvent(self, event):
        self.type = self.type_deque.popleft()
        self.type_deque.append(self.type)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = GridWindow(4, 8)
    app.exec_()
