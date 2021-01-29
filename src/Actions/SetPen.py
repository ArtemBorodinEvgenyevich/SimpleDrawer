from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets, QtGui


class SetPenAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setIcon(QtGui.QIcon("./icons/pen_ico.png"))
        self.setText("Pen")
        self.setToolTip("Choose Pen tool")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().setTool(ToolEnum.PEN)
