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

    def gaussianBlur(self, pixmap: QtGui.QPixmap, radius: int):
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem()
        item.setPixmap(pixmap)
        blur = QtWidgets.QGraphicsBlurEffect()
        blur.setBlurRadius(radius)
        item.setGraphicsEffect(blur)
        scene.addItem(item)
        result = QtGui.QImage(pixmap.size(), QtGui.QImage.Format_ARGB32)
        result.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(result)
        scene.render(painter, QtCore.QRectF(), QtCore.QRectF(0,0, pixmap.width(), pixmap.height()))
        painter.end()

        return QtGui.QPixmap.fromImage(result)

