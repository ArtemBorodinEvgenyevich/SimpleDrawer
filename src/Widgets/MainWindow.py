from PyQt5 import QtWidgets, QtCore, QtGui
from src.Widgets.MenuBar import MenuBar
from src.Widgets.ViewArea import ViewArea
from src.Widgets.Canvas import Canvas
from src.Widgets.ColorPalette import PaletteHorizontal

from src.Actions.NewFile import NewFileAction
from src.Actions.ImportImage import ImportFileAction

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.menu = MenuBar()
        self.canvas = Canvas()
        self.viewArea = ViewArea()
        self.colorPalette = PaletteHorizontal("32poly")

        self.newFileAction = NewFileAction(self)
        self.newFromImageAction = ImportFileAction(self)

        self._initUI()

    def _initUI(self):
        self.setMenuBar(self.menu)
        self.viewArea.setWidget(self.canvas)

        container = QtWidgets.QWidget()
        container.setLayout(QtWidgets.QVBoxLayout())

        container.layout().addWidget(self.colorPalette)
        container.layout().addWidget(self.viewArea)

        self.setCentralWidget(container)

        self.colorPalette.selected.connect(self.canvas.setPenColor)

        self.menu.fileMenu.addAction(self.newFileAction)
        self.menu.fileMenu.addAction(self.newFromImageAction)

    def setNewCanvas(self, width=640, height=480):
        self.canvas.setPixmap(QtGui.QPixmap(width, height))
        self.canvas.pixmap().fill(QtCore.Qt.white)
        self.canvas.resize(self.canvas.pixmap().size())

    def setNewCanvasFromFile(self, filePath):
        self.canvas.setPixmap(QtGui.QPixmap(filePath))
        self.canvas.resize(self.canvas.pixmap().size())








