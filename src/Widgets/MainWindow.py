from PySide2 import QtWidgets
from src.Widgets.CentralWidget import CentralWidget
from src.Widgets.MenuBar import MenuBar
from src.Widgets.Actions.NewFile import NewFileAction

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.menuBar = MenuBar()
        self.toolBar = self.addToolBar("Actions")
        self.central = CentralWidget()

        self.setCentralWidget(self.central)
        self.setMenuBar(self.menuBar)
        self.setupMenu()


    def setupMenu(self):
        self.newFileAction = NewFileAction()

        self.menuBar.fileMenu.addAction(self.newFileAction)


