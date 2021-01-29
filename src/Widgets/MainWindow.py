from PyQt5 import QtWidgets, QtCore, QtGui
from src.Widgets.MenuBar import MenuBar
from src.Widgets.ViewArea import ViewArea
from src.Widgets.Canvas import Canvas
from src.Widgets.ColorPalette import PaletteHorizontal

from src.Actions.NewFile import NewFileAction
from src.Actions.ImportImage import ImportFileAction
from src.Actions.SaveImage import SaveImageAction
from src.Actions.MakeGrayscale import MakeGrayscaleAction
from src.Actions.BlurImage import BlurImageAction
from src.Actions.SetPen import SetPenAction
from src.Actions.SetSpray import SetSprayAction
from src.Actions.SetRubber import SetRubberAction
from src.Actions.SetFill import SetFillAction

from src.Maths.ImageProcessor import ImageProcessor
from src.Enums.ToolEnum import ToolEnum


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.toolBar = QtWidgets.QToolBar()
        self.menu = MenuBar()
        self.canvas = Canvas()
        self.viewArea = ViewArea()
        self.colorPalette = PaletteHorizontal("32poly")
        self.toolSize = QtWidgets.QSpinBox()
        self.particlesAmount = QtWidgets.QSpinBox()


        self.newFileAction = NewFileAction(self)
        self.newFromImageAction = ImportFileAction(self)
        self.saveImageAction = SaveImageAction(self)

        self.makeImageGrayscaleAction = MakeGrayscaleAction(self)
        self.blurImageAction = BlurImageAction(self)

        self.setPenAction = SetPenAction(self)
        self.setSprayAction = SetSprayAction(self)
        self.setRubberAction = SetRubberAction(self)
        self.setFillAction = SetFillAction(self)


        self._initUI()

    def _initUI(self):
        self.addToolBar(self.toolBar)
        self.toolBar.setMovable(False)
        #self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.toolSize.setToolTip("Set tool size")
        self.toolSize.setValue(self.canvas.getToolSize())
        self.toolSize.setMinimumWidth(50)
        self.toolSize.setMaximum(4096)
        self.particlesAmount.setToolTip("Set spray particles amount")
        self.particlesAmount.setValue(self.canvas.getParticlesAmount())
        self.particlesAmount.setMinimumWidth(50)
        self.particlesAmount.setMaximum(4096)

        self.setMenuBar(self.menu)
        self.viewArea.setWidget(self.canvas)

        container = QtWidgets.QWidget()
        container.setLayout(QtWidgets.QVBoxLayout())

        container.layout().addWidget(self.colorPalette)
        container.layout().addWidget(self.viewArea)

        self.setCentralWidget(container)

        self.colorPalette.selected.connect(self.canvas.setToolColor)
        self.toolSize.valueChanged.connect(self.canvas.setToolSize)
        self.particlesAmount.valueChanged.connect(self.canvas.setParticlesAmount)

        self.toolBar.addAction(self.setPenAction)
        self.toolBar.addAction(self.setSprayAction)
        self.toolBar.addAction(self.setFillAction)
        self.toolBar.addAction(self.setRubberAction)

        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.toolSize)
        self.toolBar.addWidget(self.particlesAmount)

        self.menu.fileMenu.addAction(self.newFileAction)
        self.menu.fileMenu.addAction(self.newFromImageAction)
        self.menu.fileMenu.addAction(self.saveImageAction)

        self.menu.editMenu.addAction(self.makeImageGrayscaleAction)
        self.menu.editMenu.addAction(self.blurImageAction)

    def setNewCanvas(self, width=640, height=480):
        self.canvas.setPixmap(QtGui.QPixmap(width, height))
        self.canvas.pixmap().fill(QtCore.Qt.transparent)
        self.canvas.resize(self.canvas.pixmap().size())
        self.canvas.setBorder()

    def setNewCanvasFromFile(self, filePath):
        self.canvas.setPixmap(QtGui.QPixmap(filePath))
        self.canvas.resize(self.canvas.pixmap().size())
        self.canvas.setBorder()

    def setTool(self, toolType: ToolEnum):
        self.canvas.setToolType(toolType)

    def saveImage(self, filePath):
        self.canvas.pixmap().save(filePath)

    def fillImage(self):
        self.canvas.fillCanvas()

    def makeImageGrayscale(self):
        if self.canvas.pixmap() is not None:
            processor = ImageProcessor()
            self.canvas.setPixmap(processor.grayscaleFromRGB(self.canvas.pixmap()))
            self.canvas.resize(self.canvas.pixmap().size())

    def makeImageBlured(self, radius: int):
        if self.canvas.pixmap() is not None:
            processor = ImageProcessor()
            self.canvas.setPixmap(processor.gaussianBlur(self.canvas.pixmap(), radius))
            self.canvas.resize(self.canvas.pixmap().size())
