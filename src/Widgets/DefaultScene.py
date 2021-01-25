from PySide2 import QtWidgets, QtGui, QtCore


class DefaultScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(DefaultScene, self).__init__(parent)

        self._prev_point = QtCore.QPointF()

    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):
        self.addEllipse(
            event.scenePos().x() - 5,
            event.scenePos().y() - 5,
            10, 10,
            QtGui.QPen(QtCore.Qt.NoPen),
            QtGui.QBrush(QtCore.Qt.red)
        )
        self._prev_point = event.scenePos()

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):

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
