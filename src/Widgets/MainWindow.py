from PySide2 import QtWidgets
from src.Widgets.CentralWidget import CentralWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.toolBar = self.addToolBar("Actions")
        self.viewport = CentralWidget()

        self.setCentralWidget(self.viewport)

