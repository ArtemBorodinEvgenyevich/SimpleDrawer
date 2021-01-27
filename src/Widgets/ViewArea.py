from PyQt5 import QtWidgets, QtGui, QtCore
from src.Widgets.Canvas import Canvas

class ViewArea(QtWidgets.QScrollArea):
    def __init__(self):
        super(ViewArea, self).__init__()
        self.setAutoFillBackground(True)
        # TODO: Custom QPalette
        self.setBackgroundRole(QtGui.QPalette.Dark)







