from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets, QtGui


class SetFillAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setIcon(QtGui.QIcon("./icons/fill_ico.png"))
        self.setText("Fill")
        self.setToolTip("Choose Fill tool")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().fillImage()
