from PySide2 import QtWidgets
import sys

from src.Widgets.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())

