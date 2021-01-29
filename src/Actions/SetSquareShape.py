from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets


class SetSquareShapeAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Square shape")
        self.setToolTip("Choose Square shape")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().setTool(ToolEnum.SQUARE)
