from PyQt5 import QtWidgets, QtCore, QtGui
from src.Dialogs.NewFileDialog import NewFileDialog


class NewFileAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("New File")
        self.setShortcut("Ctrl+N")
        self.triggered.connect(self._newFile)

        self.dialog = NewFileDialog()

    def _newFile(self):
        if self.dialog.exec_():
            pageSize = self.dialog.getPageSize()
            self.parent().setCanvas(pageSize.width(), pageSize.height())





