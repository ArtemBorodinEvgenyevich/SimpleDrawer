from PyQt5 import QtWidgets, QtCore, QtGui


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.last_x, self.last_y = None, None
        self.penColor = QtGui.QColor('#000000')

    def setPenColor(self, color):
        self.penColor = QtGui.QColor(color)

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.penColor)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
