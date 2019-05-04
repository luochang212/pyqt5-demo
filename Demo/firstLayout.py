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
        
        # create new buttons
        self.btn_left = QPushButton('left', self)
        self.btn_right = QPushButton('right', self)

        # setting up a layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.btn_left)
        main_layout.addWidget(self.btn_right)

        # create the central widget
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
