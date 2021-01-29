from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets, QtGui


class SetSprayAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setIcon(QtGui.QIcon("./icons/spray_ico.png"))
        self.setText("Spray")
        self.setToolTip("Choose Spray tool")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().setTool(ToolEnum.SPRAY)
