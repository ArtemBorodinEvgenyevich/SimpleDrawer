from PyQt5 import QtWidgets, QtCore, QtGui
from src.Widgets.MenuBar import MenuBar
from src.Widgets.ViewArea import ViewArea
from src.Widgets.Canvas import Canvas
from src.Widgets.ColorPalette import PaletteHorizontal

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.menu = MenuBar()
        self.canvas = Canvas()
        self.viewArea = ViewArea()
        self.colorPalette = PaletteHorizontal("32poly")

        self._initUI()
        self.setCanvas()

    def _initUI(self):
        self.setMenuBar(self.menu)
        self.viewArea.setWidget(self.canvas)

        container = QtWidgets.QWidget()
        container.setLayout(QtWidgets.QVBoxLayout())

        container.layout().addWidget(self.colorPalette)
        container.layout().addWidget(self.viewArea)

        self.setCentralWidget(container)

        self.colorPalette.selected.connect(self.canvas.setPenColor)

    def setCanvas(self):
        self.canvas.setPixmap(QtGui.QPixmap(640, 480))
        self.canvas.pixmap().fill(QtCore.Qt.white)
        self.canvas.resize(self.canvas.pixmap().size())








