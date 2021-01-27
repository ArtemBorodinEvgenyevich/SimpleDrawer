from PyQt5 import QtWidgets, QtCore, QtGui
from src.Dialogs.NewFileDialog import NewFileDialog


class NewFileAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("New File")
        self.setShortcut("Ctrl+N")
        self.triggered.connect(self._newFile)

        self._dialog = NewFileDialog()

    def _newFile(self):
        if self._dialog.exec_():
            pageSize = self._dialog.getPageSize()
            self.parent().setNewCanvas(pageSize.width(), pageSize.height())





