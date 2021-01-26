from PySide2 import QtWidgets, QtCore


class NewFileDialog(QtWidgets.QDialog):
    def __init__(self):
        super(NewFileDialog, self).__init__()

        self._canvasWidth = 0
        self._canvasHeigth = 0

        self._initUI()

    def _initUI(self):
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)

        tabWidget = QtWidgets.QTabWidget()
        mainLayout.addWidget(tabWidget)

        self.buttonBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        mainLayout.addWidget(self.buttonBox)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.setCanvasSize)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.reject)

        # First tab layout
        self.widthSpin = QtWidgets.QSpinBox()
        self.widthSpin.setToolTip("Max resolution: 4096x4096")
        self.widthSpin.setRange(1, 4096)

        self.heightSpin = QtWidgets.QSpinBox()
        self.heightSpin.setToolTip("Max resolution: 4096x4096")
        self.heightSpin.setRange(1, 4096)

        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Width:", self.widthSpin)
        formLayout.addRow("Height:", self.heightSpin)

        firstGroup = QtWidgets.QGroupBox("Canvas size")
        firstGroup.setLayout(formLayout)

        tabWidget.addTab(firstGroup, "Create empty canvas")

        # TODO: implement functionality
        # Second tab layout
        self.pathBtn = QtWidgets.QPushButton("...")
        self.pathBtn.setToolTip("Click to choose image path")
        self.pathBtn.setFixedWidth(30)

        self.pathTextLine = QtWidgets.QLineEdit()
        self.pathTextLine.setToolTip("Choose file path")

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.setAlignment(QtCore.Qt.AlignCenter)
        hLayout.addWidget(self.pathTextLine)
        hLayout.addWidget(self.pathBtn)

        secondGroup = QtWidgets.QGroupBox("Image path")
        secondGroup.setLayout(hLayout)

        tabWidget.addTab(firstGroup, "Empty canvas")
        tabWidget.addTab(secondGroup, "Create canvas from image")


    def setCanvasSize(self):
        self._canvasWidth = self.widthSpin.value()
        self._canvasHeigth = self.heightSpin.value()
        self.accept()

    def getCanvasSize(self):
        return self._canvasWidth, self._canvasHeigth
