from PyQt5 import QtWidgets, QtGui, QtCore


class ImageProcessor():
    def __init__(self):
        super().__init__()

    def grayscaleFromRGB(self, pixmap: QtGui.QPixmap):
        image = pixmap.toImage()

        for i in range(image.width()):
            for j in range(image.height()):
                gray = QtGui.qGray(image.pixel(i, j))
                image.setPixel(i, j, QtGui.QColor(gray, gray, gray).rgb())

        return QtGui.QPixmap.fromImage(image)

