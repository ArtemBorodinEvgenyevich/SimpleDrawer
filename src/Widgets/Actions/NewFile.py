from PySide2 import QtWidgets, QtCore
from src.Widgets.Dialogs.NewFileDialog import NewFileDialog

class NewFileAction(QtWidgets.QAction):
    def __init__(self):
        super(NewFileAction, self).__init__()
        self.setText("New File")
        self.setShortcut("Ctrl+N")
        self.connect(QtCore.SIGNAL("triggered()"), self.newFile)

    def newFile(self):
        dialog = NewFileDialog()
        print(dialog.exec_())
