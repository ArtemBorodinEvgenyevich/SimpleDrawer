import random
from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets, QtCore, QtGui


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self._last_x, self._last_y = None, None
        self._particlesAmount = 100
        self._toolColor = QtGui.QColor('#000000')
        self._toolSize = 10
        self._toolType = ToolEnum.PEN
        self._frameWidth = 5

    def setToolColor(self, color):
        self._toolColor = QtGui.QColor(color)

    def mouseMoveEvent(self, e):
        if self._toolType is ToolEnum.PEN:
            self._penDraw(e)
        elif self._toolType is ToolEnum.SPRAY:
            self._sprayDraw(e)
        elif self._toolType is ToolEnum.RUBBER:
            self._rubberErase(e)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self._toolType is ToolEnum.SQUARE:
            self._drawSquare(ev)
        elif self._toolType is ToolEnum.CIRCLE:
            self._drawCircle(ev)

    def mouseReleaseEvent(self, e):
        self._last_x = None
        self._last_y = None

    def setToolType(self, toolType: ToolEnum):
        self._toolType = toolType

    def setToolSize(self, px: int):
        self._toolSize = px

    def getToolSize(self):
        return self._toolSize

    def setParticlesAmount(self, amount: int):
        self._particlesAmount = amount

    def getParticlesAmount(self):
        return self._particlesAmount

    def setFrameWidth(self, px: int):
        self._frameWidth = px

    def getFrameWidth(self):
        return self._frameWidth

    def setBorder(self):
        if self.pixmap() is not None:
            self.setStyleSheet("border: 5px dot-dot-dash yellow")
            self.update()

    def fillCanvas(self):
        self.pixmap().fill(self._toolColor)
        self.update()

    def createCursor(self):
        pixmap = QtGui.QPixmap(QtCore.QSize(1, 1) * self._toolSize)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))
        painter.drawRect(pixmap.rect())
        painter.end()
        cursor = QtGui.QCursor(pixmap)
        QtWidgets.QApplication.setOverrideCursor(cursor)

    def _penDraw(self, e):
        if self._last_x is None:  # First event.
            self._last_x = e.x()
            self._last_y = e.y()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        p = painter.pen()
        p.setWidth(self._toolSize)
        p.setColor(self._toolColor)
        painter.setPen(p)
        painter.drawLine(self._last_x, self._last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self._last_x = e.x()
        self._last_y = e.y()

    def _sprayDraw(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self._toolColor)
        painter.setPen(p)

        for n in range(self._particlesAmount):
            xo = random.gauss(0, self._toolSize)
            yo = random.gauss(0, self._toolSize)
            painter.drawPoint(e.x() + xo, e.y() + yo)

        self.update()

    def _rubberErase(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.save()
        p = painter.pen()
        p.setColor(QtCore.Qt.transparent)
        painter.setPen(p)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_Clear)
        rect = QtCore.QRect(QtCore.QPoint(), self._toolSize*QtCore.QSize())
        rect.moveCenter(e.pos())
        painter.eraseRect(rect)
        painter.restore()
        painter.end()
        self.update()

    def _drawSquare(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        p = painter.pen()
        p.setWidth(self._frameWidth)
        p.setColor(self._toolColor)
        painter.setPen(p)
        rect = QtCore.QRect(QtCore.QPoint(), self._toolSize*QtCore.QSize())
        rect.moveCenter(e.pos())
        painter.drawRect(rect)
        painter.end()
        self.update()

    def _drawCircle(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        p = painter.pen()
        p.setWidth(self._frameWidth)
        p.setColor(self._toolColor)
        painter.setPen(p)
        rect = QtCore.QRect(QtCore.QPoint(), self._toolSize*QtCore.QSize())
        rect.moveCenter(e.pos())
        painter.drawEllipse(rect)
        painter.end()
        self.update()



