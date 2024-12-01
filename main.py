import sys
import random
from PyQt6 import QtWidgets, uic, QtGui


class CircleApp(QtWidgets.QWidget):
    def __init__(self):
        super(CircleApp, self).__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, 400 - diameter)
        y = random.randint(0, 400 - diameter)
        color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = QtWidgets.QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QtGui.QBrush(color))
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec())