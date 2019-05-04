from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('My first window - www.luochang.ink')

        # set the size of window
        self.Width = 500
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        self.initUI()

    def initUI(self):

        # create a new button
        self.btn = QPushButton('first Button', self)
        self.btn.resize(300,90)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
