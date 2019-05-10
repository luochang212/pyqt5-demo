from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Sidebar layout - www.luochang.ink')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('Text', self)
        self.btn_2 = QPushButton('Show', self)
        self.btn_3 = QPushButton('Plot', self)
        self.btn_4 = QPushButton('copyright', self)

        self.btn_1.setObjectName('left_button')
        self.btn_2.setObjectName('left_button')
        self.btn_3.setObjectName('left_button')
        self.btn_4.setObjectName('left_button')

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)

        self.btn_ui1_1 = QPushButton('Clean', self)
        self.btn_ui1_2 = QPushButton('Show And Plot', self)

        self.btn_ui1_1.clicked.connect(self.text_clean)
        self.btn_ui1_2.clicked.connect(self.text_show)

        self.textBox = QTextEdit(self)

        self.showText = QLabel('')

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        # initialize variable
        self.strList = np.array([])

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:rgb(0,0,0);
                font-size:20px;
                font-weight:400;
                text-align:left;
            }
            QPushButton#left_button:hover{
                font-weight:600;
                background:rgb(220,220,220);
                border-left:5px solid blue;
            }
            QWidget#left_widget{
                background:rgb(220,220,220);
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ----------------- 
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)
        self.clean()
        self.btn_1.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    def button2(self):
        self.right_widget.setCurrentIndex(1)
        self.clean()
        self.btn_2.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    def button3(self):
        self.right_widget.setCurrentIndex(2)
        self.clean()
        self.btn_3.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    def button4(self):
        self.right_widget.setCurrentIndex(3)
        self.clean()
        self.btn_4.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    # ----------------- 
    # functions

    def clean(self):
        self.btn_1.setStyleSheet('''''')
        self.btn_2.setStyleSheet('''''')
        self.btn_3.setStyleSheet('''''')
        self.btn_4.setStyleSheet('''''')

    def text_clean(self):
        self.textBox.setText('')

    def text_show(self):
        self.showText.setText(self.textBox.toPlainText())

        string = str(self.textBox.toPlainText())
        for i in range(len(string)):
            self.strList = np.append(self.strList, string[i])
        self.plot()
        self.strList = np.array([])

    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set(xlabel="character", ylabel="frequency")
        ax.set(title="The frequency of characters")
        ax.hist(self.strList, bins=24)
        self.canvas.draw()
        
    # ----------------- 
    # pages

    def ui1(self):
        upper_layout = QHBoxLayout()
        upper_layout.addWidget(self.btn_ui1_1)
        upper_layout.addWidget(self.btn_ui1_2)
        upper = QWidget()
        upper.setLayout(upper_layout)
        main_layout = QVBoxLayout()
        main_layout.addWidget(upper)
        main_layout.addWidget(self.textBox)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.showText)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
        
    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        ui4_label1 = QLabel('Sidebar Layout Demo')
        ui4_label1.setStyleSheet('''color:white;font-size:45px;background:rgb(200,220,220);''')
        ui4_label2 = QLabel('Author: Chang Luo\nGender: male\nWebsite: luochang212.github.io\nAvailable: yes')
        ui4_label2.setStyleSheet('''font-size:20px;''')
        ui4_label3 = QLabel('© 2019 chang luo')

        footer_layout = QHBoxLayout()
        footer_layout.addStretch(5)
        footer_layout.addWidget(ui4_label3)

        main_layout = QVBoxLayout()
        main_layout.addWidget(ui4_label1)
        main_layout.addWidget(ui4_label2)
        main_layout.addStretch(10)
        main_layout.addLayout(footer_layout)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
