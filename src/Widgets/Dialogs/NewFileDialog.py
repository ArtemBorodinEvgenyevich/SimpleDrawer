from PySide2 import QtWidgets, QtCore


class NewFileDialog(QtWidgets.QDialog):
    def __init__(self):
        super(NewFileDialog, self).__init__()

        self._canvasWidth = 640
        self._canvasHeigth = 480

        self.setSizeGripEnabled(True)

    def _initUI(self):
        self.widthSpin = QtWidgets.QSpinBox()
        self.widthSpin.setMaximum(4096)
        self.widthSpin.setRange(1, 4096)

        self.heightSpin = QtWidgets.QSpinBox()
        self.heightSpin.setMaximum(4096)
        self.heightSpin.setRange(1, 4096)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok,
                                                    QtCore.Qt.Horizontal, self)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.widthSpin)
        hLayout.addWidget(self.heightSpin)

        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.buttonBox)

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.getCanvasSize())


    def getCanvasSize(self):
        self._canvasWidth = self.widthSpin.value()
        self._canvasHeigth = self.heightSpin.value()
        self.close()

        return self._canvasWidth, self._canvasHeigth
