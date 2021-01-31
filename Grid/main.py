from PyQt5.QtWidgets import QApplication
from frontend.main_window import GridWindow
from grid import Grid
import sys

if __name__ == "__main__":
    app = QApplication([])
    grid = Grid(50, 50)
    window = GridWindow(grid.rows, grid.columns)

    #  Conexion de Señales
    window.senal_cambiar_estilo.connect(grid.change_type)
    app.exec_()
