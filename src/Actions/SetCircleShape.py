from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets


class SetCircleShapeAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Circle shape")
        self.setToolTip("Choose Circle shape")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().setTool(ToolEnum.CIRCLE)
