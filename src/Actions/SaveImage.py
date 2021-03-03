import os
from PyQt5 import QtWidgets, QtCore



class SaveImageAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Save Image")
        self.setToolTip("Save image to file")
        self.triggered.connect(self._saveImage)


    def _saveImage(self):
        if self.parent().canvas.pixmap() is not None:
            file, ok = QtWidgets.QFileDialog.getSaveFileName(
                self.parent(),
                'Save Image',
                f'{os.path.expanduser("~")}',
                'Image File (*.bmp *.jpg *.jpeg *.png)'
            )
            if ok:
                self.parent().saveImage(file)


