import os
from PyQt5 import QtWidgets, QtGui, QtCore


class ImportFileAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Create from image")
        self.setToolTip("Create new file from image")
        self.triggered.connect(self._importImage)

    def _importImage(self):
        file, ok = QtWidgets.QFileDialog.getOpenFileName(
            self.parent(),
            'Import Image',
            f'{os.path.expanduser("~")}',
            'Image File (*.bmp *.jpg *.jpeg *.png)'
        )
        if ok:
            self.parent().setNewCanvasFromFile(file)
