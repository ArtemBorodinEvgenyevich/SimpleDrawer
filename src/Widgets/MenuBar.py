from PySide2 import QtWidgets

class MenuBar(QtWidgets.QMenuBar):
    def __init__(self):
        super(MenuBar, self).__init__()

        self.fileMenu = QtWidgets.QMenu("&File", self)

        self.addMenu(self.fileMenu)