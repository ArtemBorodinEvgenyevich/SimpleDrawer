from PyQt5 import QtWidgets, QtCore


class NewFileDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.btnBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal
        )

        self._pageWidth = 0
        self._pageHeight = 0

        self._pageWidthSpin = QtWidgets.QSpinBox()
        self._pageHeightSpin = QtWidgets.QSpinBox()

        self._initUI()

    def _initUI(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setWindowTitle("New file")

        self._pageWidthSpin.setRange(10, 4096)
        self._pageWidthSpin.setToolTip("Range: from 10 to 4096")
        self._pageHeightSpin.setRange(10, 4096)
        self._pageHeightSpin.setToolTip("Range: from 10 to 4096")

        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Width:", self._pageWidthSpin)
        formLayout.addRow("Height:", self._pageHeightSpin)

        groupBox = QtWidgets.QGroupBox("Create new file")
        groupBox.setLayout(formLayout)
        self.layout().addWidget(groupBox)
        self.layout().addWidget(self.btnBox)

        self.btnBox.accepted.connect(self._setPageSizeValues)
        self.btnBox.rejected.connect(self.reject)

    def _setPageSizeValues(self):
        self._pageWidth = self._pageWidthSpin.value()
        self._pageHeight = self._pageHeightSpin.value()
        self.accept()

    def getPageSize(self):
        return QtCore.QSize(self._pageWidth, self._pageHeight)