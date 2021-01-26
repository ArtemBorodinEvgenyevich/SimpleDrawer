from PySide2 import QtWidgets, QtCore
from src.Dialogs.NewFileDialog import NewFileDialog

class NewFileAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super(NewFileAction, self).__init__(parent)
        self.setText("New File")
        self.setShortcut("Ctrl+N")
        self.connect(QtCore.SIGNAL("triggered()"), self.newFile)

    def newFile(self):
        dialog = NewFileDialog()
        if dialog.exec_():
            size = dialog.getCanvasSize()
            self.parent().central.clearCanvas()
            self.parent().central.setCanvas(*size)
