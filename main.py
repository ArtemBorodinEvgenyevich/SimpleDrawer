import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from src.Widgets.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())

