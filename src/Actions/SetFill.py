from PyQt5 import QtWidgets


class SetFillAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Fill")
        self.setToolTip("Choose Fill tool")
        self.triggered.connect(self._setTool)

    def _setTool(self):
        self.parent().fillImage()
