from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5 import uic


class GridWindow(QWidget):
    def __init__(self):
        super(GridWindow, self).__init__()
        uic.loadUi('grid_solver.ui', self)
        print("oliwis")
        self.show()


class Square(QLabel):
    """
    Defines each square of the grid, it can be swaped from normal, wall, start, goal
    """


if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = GridWindow()
    app.exec_()
