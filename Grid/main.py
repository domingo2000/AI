from PyQt5.QtWidgets import QApplication
from frontend.main_window import GridWindow
from Ai.searching import SearchSolver
from grid import Grid

import sys

if __name__ == "__main__":
    app = QApplication([])
    grid = Grid(10, 10)
    solver = SearchSolver((2, 2), grid.neighbours, grid.is_goal)
    window = GridWindow(grid.rows, grid.columns)

    #  Conexion de Señales
    window.senal_cambiar_estilo.connect(grid.change_type)
    window.senal_llamar_vecinos.connect(grid.neighbours)
    window.senal_resolver_camino.connect(solver.solve)
    solver.senal_pintar_recorrido.connect(window.paint_path)
    solver.senal_pintar_frontera.connect(window.paint_frontier)
    solver.senal_pintar_solucion.connect(window.paint_solution)
    app.exec_()
