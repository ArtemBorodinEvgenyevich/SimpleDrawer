from PySide2 import QtWidgets, QtGui, QtCore


class DefaultScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(DefaultScene, self).__init__()

        self._prev_point = QtCore.QPointF()
        self._pageSize = QtCore.QSize()
        self._canvasRect = None
        self._canDraw = False


    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):

        if self.items() != 0 and event.button() & QtCore.Qt.LeftButton:
            if self._canDraw:
                self.addEllipse(
                    event.scenePos().x() - 5,
                    event.scenePos().y() - 5,
                    10, 10,
                    QtGui.QPen(QtCore.Qt.NoPen),
                    QtGui.QBrush(QtCore.Qt.red)
                )
        self._prev_point = event.scenePos()

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):
        if self.items() != 0 and event.button() & QtCore.Qt.LeftButton:
            if self._canDraw:
                print("kek")

                self.addLine(
                    self._prev_point.x(),
                    self._prev_point.y(),
                    event.scenePos().x(),
                    event.scenePos().y(),
                    QtGui.QPen(
                        QtCore.Qt.red, 10,
                        QtCore.Qt.SolidLine,
                        QtCore.Qt.RoundCap
                    )
                )
        self._prev_point = event.scenePos()

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        painter.setBrush(QtGui.QBrush(QtGui.QColor(74, 74, 74)))
        painter.drawRect(rect)

    def setDrawable(self, can_draw: bool):
        """Set flag for drawing ability"""
        self._canDraw = can_draw

    def getCanvas(self):
        """Return canvas pointer"""
        return self._canvasRect

    def _setupPage(self, width, height):
        """Canvas setup"""
        self._pageSize = QtCore.QSize(width, height)
        self.addRect(
            0,0,
            width, height,
            QtGui.QPen(QtCore.Qt.NoPen),
            QtGui.QBrush(QtCore.Qt.white)
        )
        self._canvasRect = self.items().pop()

    def _clearPage(self):
        """Removing canvas and all elements"""
        if self.items().count() != 0:
            for item in self.items():
                self.removeItem(item)
        return







