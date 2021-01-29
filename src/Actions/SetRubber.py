from src.Enums.ToolEnum import ToolEnum
from PyQt5 import QtWidgets


class SetRubberAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Rubber")
        self.setToolTip("Choose Rubber tool")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().setTool(ToolEnum.RUBBER)
