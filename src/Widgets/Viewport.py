from PySide2 import QtWidgets, QtGui, QtCore


class Viewport(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent)

        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setRenderHint(QtGui.QPainter.TextAntialiasing)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

    def setActive(self, scene: QtWidgets.QGraphicsScene):
        """Set scene and activate"""
        self.setScene(scene)
        self.scene().setParent(self)

    def createCanvas(self, width, height):
        """Interface to create a canvas"""
        self.scene()._setupPage(width, height)

    def clearCanvas(self):
        self.scene()._clearPage()
        self.scene().deleteLater()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if self.items() != 0:
            if self.itemAt(event.pos()) == self.scene().getCanvas():
                self.scene().setDrawable(True)
            else:
                self.scene().setDrawable(False)
        
        super(Viewport, self).mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.buttons() & QtCore.Qt.RightButton:
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

        if self.items() != 0:
            if event.buttons() & QtCore.Qt.LeftButton:
                print(self.itemAt(event.pos()))
                if self.itemAt(event.pos()) == self.scene().getCanvas():
                    self.scene().setDrawable(True)

        super(Viewport, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        if event.buttons() & QtCore.Qt.RightButton:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        super(Viewport, self).mouseReleaseEvent(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() and QtCore.Qt.Key_Alt:
            self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        super(Viewport, self).keyPressEvent(event)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        if event.key() and QtCore.Qt.Key_Alt:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        super(Viewport, self).keyReleaseEvent(event)








