from PyQt5 import QtWidgets, QtGui, QtCore
from src.Widgets.Canvas import Canvas

class ViewArea(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super(ViewArea, self).__init__(parent)
        self.setAutoFillBackground(True)
        # TODO: Custom QPalette
        self.setBackgroundRole(QtGui.QPalette.Dark)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.parent().parent().canvas.createCursor()

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        QtWidgets.QApplication.restoreOverrideCursor()







