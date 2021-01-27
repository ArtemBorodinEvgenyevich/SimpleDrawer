from PyQt5 import QtWidgets, QtCore, QtGui
from src.Widgets.MenuBar import MenuBar
from src.Widgets.ViewArea import ViewArea
from src.Widgets.Canvas import Canvas
from src.Widgets.ColorPalette import PaletteHorizontal

from src.Actions.NewFile import NewFileAction
from src.Actions.ImportImage import ImportFileAction
from src.Actions.SaveImage import SaveImageAction
from src.Actions.MakeGrayscale import MakeGrayscaleAction

from src.Maths.ImageProcessor import ImageProcessor

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.menu = MenuBar()
        self.canvas = Canvas()
        self.viewArea = ViewArea()
        self.colorPalette = PaletteHorizontal("32poly")

        self.newFileAction = NewFileAction(self)
        self.newFromImageAction = ImportFileAction(self)
        self.saveImageAction = SaveImageAction(self)

        self.makeImageGrayscaleAction = MakeGrayscaleAction(self)

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
        self.menu.fileMenu.addAction(self.saveImageAction)

        self.menu.editMenu.addAction(self.makeImageGrayscaleAction)

    def setNewCanvas(self, width=640, height=480):
        self.canvas.setPixmap(QtGui.QPixmap(width, height))
        self.canvas.pixmap().fill(QtCore.Qt.white)
        self.canvas.resize(self.canvas.pixmap().size())

    def setNewCanvasFromFile(self, filePath):
        self.canvas.setPixmap(QtGui.QPixmap(filePath))
        self.canvas.resize(self.canvas.pixmap().size())

    def saveImage(self, filePath):
        self.canvas.pixmap().save(filePath)

    def makeImageGrayscale(self):
        if self.canvas.pixmap() is not None:
            processor = ImageProcessor()
            self.canvas.setPixmap(processor.grayscaleFromRGB(self.canvas.pixmap()))
            self.canvas.resize(self.canvas.pixmap().size())








