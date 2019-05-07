from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Sidebar layout - www.luochang.ink')

        # set the size of window
        self.Width = 500
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        self.btn_1 = QPushButton('Load', self)
        self.btn_2 = QPushButton('1', self)
        self.btn_3 = QPushButton('2', self)
        self.btn_4 = QPushButton('3', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)

        self.btn_ui1_1 = QPushButton('Load file', self)
        self.btn_ui1_2 = QPushButton('Show file', self)

        self.btn_ui1_1.clicked.connect(self.load_file)
        self.btn_ui1_2.clicked.connect(self.show_file)

        self.text = QTextEdit(self)

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QWidget()

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def button1(self):
        self.right_widget = self.ui1()

    def button2(self):
        self.right_widget = self.ui2()

    def button3(self):
        self.right_widget = self.ui3()

    def button4(self):
        self.right_widget = self.ui4()

    def load_file(self):
        print('ttt')

    def show_file(self):
        print('ttt')
        
    def ui1(self):
        upper_layout = QHBoxLayout()
        upper_layout.addWidget(self.btn_ui1_1)
        upper_layout.addWidget(self.btn_ui1_2)
        upper = QWidget()
        upper.setLayout(upper_layout)
        main_layout = QVBoxLayout()
        main_layout.addWidget(upper)
        main_layout.addWidget(self.text)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('aaa'))
        main_layout.addWidget(QLabel('aaa'))
        main = QWidget()
        main.setLayout(main_layout)
        return main
        
    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('bbb'))
        main_layout.addWidget(QLabel('ccc'))
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('ddd'))
        main_layout.addWidget(QLabel('eee'))
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
