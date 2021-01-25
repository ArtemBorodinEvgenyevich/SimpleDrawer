from PySide2 import QtCore, QtWidgets, QtGui
from src.Widgets.DefaultScene import DefaultScene

class CentralWidget(QtWidgets.QWidget):
    def __init__(self):
        super(CentralWidget, self).__init__()
        self._bgColorPrim = QtGui.QColor(74, 74, 74)
        self._bgColorSecond = QtGui.QColor(114, 114, 114)

        self.setLayout(QtWidgets.QHBoxLayout())
        self.viewport = QtWidgets.QGraphicsView()

        self.setCanvas()

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(self._bgColorPrim))
        painter.setBrush(QtGui.QBrush(self._bgColorPrim))
        painter.drawRect(0, 0, self.width(), self.height())

        painter.setPen(QtGui.QPen(self._bgColorSecond))
        painter.setBrush(QtGui.QBrush(self._bgColorSecond, QtCore.Qt.Dense7Pattern))
        painter.drawRect(0, 0, self.width(), self.height())

    def setCanvas(self, width=640, height=480):
        self.viewport.setScene(DefaultScene())
        self.viewport.setSceneRect(0, 0, width, height)

        self.layout().addWidget(self.viewport)
