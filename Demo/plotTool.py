from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import matplotlib.pyplot as plt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Plot tool - www.luochang.ink')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # create widgets
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.typeBox = QComboBox()
        self.typeBox.addItem('line chart')
        self.typeBox.addItem('scatter chart')

        self.titleBox = QLineEdit("Graph", self)
        self.xLabelBox = QLineEdit("x", self)
        self.yLabelBox = QLineEdit("y", self)

        self.xBox = QLineEdit("1,2,3,4,5", self)
        self.yBox = QLineEdit("23,32,53,75,23", self)

        self.btn_plot = QPushButton("plot", self)
        self.btn_plot.clicked.connect(self.plot)
        
        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.toolbar)
        left_layout.addWidget(self.canvas)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("type of Chart:"))
        right_layout.addWidget(self.typeBox)
        right_layout.addWidget(QLabel("title:"))
        right_layout.addWidget(self.titleBox)
        right_layout.addWidget(QLabel("x label:"))
        right_layout.addWidget(self.xLabelBox)
        right_layout.addWidget(QLabel("y label:"))
        right_layout.addWidget(self.yLabelBox)

        right_layout.addWidget(QLabel("x value:"))
        right_layout.addWidget(self.xBox)
        right_layout.addWidget(QLabel("y value:"))
        right_layout.addWidget(self.yBox)
        right_layout.addStretch(5)
        right_layout.addWidget(self.btn_plot)
        right_widget = QGroupBox("Input")
        right_widget.setLayout(right_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)
        main_layout.setStretch(0, 4)
        main_layout.setStretch(1, 1)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def plot(self):
        g_type = str(self.typeBox.currentText())

        x_data = str(self.xBox.text())
        y_data = str(self.yBox.text())

        x = np.array(x_data.split(",")).astype(np.float)
        y = np.array(y_data.split(",")).astype(np.float)

        if len(x) != len(y):
            QMessageBox.question(self, 'Message', "The size of X and Y is different. ", QMessageBox.Ok, QMessageBox.Ok)
        else:
            ax = self.figure.add_subplot(111)
            ax.clear()
            ax.set(xlabel=str(self.xLabelBox.text()), ylabel=str(self.yLabelBox.text()))
            ax.set(title=str(self.titleBox.text()))

            if g_type == 'line chart':
                ax.plot(x, y)
            elif g_type == 'scatter chart':
                ax.scatter(x, y)
            else:
                print("error.")

            self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
