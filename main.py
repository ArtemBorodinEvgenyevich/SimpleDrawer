from PySide2 import QtWidgets
import sys

import sys, os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from src.Widgets.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())

