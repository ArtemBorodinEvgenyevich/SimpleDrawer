from PyQt5 import QtWidgets


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self):
        super(MenuBar, self).__init__()

        self.fileMenu = QtWidgets.QMenu("&File", self)
        self.editMenu = QtWidgets.QMenu("&Edit", self)

        self.addMenu(self.fileMenu)
        self.addMenu(self.editMenu)
