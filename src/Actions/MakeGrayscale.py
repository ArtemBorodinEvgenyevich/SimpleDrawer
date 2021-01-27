from PyQt5 import QtWidgets


class MakeGrayscaleAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Image to grayscale")
        self.setToolTip("Make image grayscale")
        self.triggered.connect(self._makeImageGrayscale)

    def _makeImageGrayscale(self):
        self.parent().makeImageGrayscale()
