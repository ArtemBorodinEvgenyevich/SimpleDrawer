from PyQt5 import QtWidgets, QtCore


class BlurImageDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.btnBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal
        )
        self._blurRadius = QtWidgets.QSlider(QtCore.Qt.Horizontal)

        self._initUI()
        self.resize(600, 50)

    def _initUI(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setWindowTitle("Set Blur radius")

        self._blurRadius.setRange(0, 100)
        self._blurRadius.setTickInterval(1)
        self._blurRadius.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self._blurRadius.setValue(0)

        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Blur Radius:", self._blurRadius)

        groupBox = QtWidgets.QGroupBox("Blur radius setup")
        groupBox.setLayout(formLayout)
        self.layout().addWidget(groupBox)
        self.layout().addWidget(self.btnBox)

        self.btnBox.accepted.connect(self.accept)
        self.btnBox.rejected.connect(self.reject)

    def getRadius(self):
        return self._blurRadius.value()
