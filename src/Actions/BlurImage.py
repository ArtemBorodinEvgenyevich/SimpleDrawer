from PyQt5 import QtWidgets, QtGui, QtCore
from src.Dialogs.BlurImageDialog import BlurImageDialog


class BlurImageAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Blur Image")
        self.setToolTip("Apply Gaussian blur to the image")
        self.triggered.connect(self._blurImage)

        self._dialog = BlurImageDialog()

    def _blurImage(self):
        if self.parent().canvas.pixmap() is not None:
            if self._dialog.exec_():
                blurRadius = self._dialog.getRadius()
                self.parent().makeImageBlured(blurRadius)

