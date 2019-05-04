from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title of main window
        self.setWindowTitle('PyQt5 desktop application - www.luochang.ink')

        # set the size of window
        self.Width = 700
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # create all widgets
        self.Label1 = QLabel("夸夸机器人 - Praise me please")
        self.Label1.setFont(QFont('bold', 14))

        self.Label2 = QLabel("created by luochang")
        self.Label2.setFont(QFont('bold', 7))

        self.nameBox = QLineEdit('你')

        self.genderBox = QComboBox()
        self.genderBox.addItem('all')
        self.genderBox.addItem('female')
        self.genderBox.addItem('male')
        
        self.advantageBox = QComboBox()
        self.advantageBox.addItem('all')
        self.advantageBox.addItem('character')
        self.advantageBox.addItem('intelligence')
        self.advantageBox.addItem('appearance')

        self.textBox = QTextEdit(self)

        self.btn = QPushButton('Praise me', self)
        self.btn.clicked.connect(self.praise_me)

        self.initUI()

    def initUI(self):
        # setting up layout of main window
        upper_widget = self.create_upper_widget()
        lower_widget = self.create_lower_widget()
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(upper_widget)
        main_layout.addWidget(lower_widget)
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 4)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def create_upper_widget(self):
        upper_layout = QVBoxLayout()
        upper_layout.addWidget(self.Label1)
        upper_layout.addStretch(5)
        upper_layout.addWidget(self.Label2)
        upper_layout.addStretch(5)
        upper_widget = QWidget()
        upper_widget.setLayout(upper_layout)
        return upper_widget

    def create_lower_widget(self):
        lower_left_widget = QGroupBox("Selections")
        lower_left_layout = QVBoxLayout()        
        lower_left_layout.addWidget(QLabel("Your name:"))
        lower_left_layout.addWidget(self.nameBox)
        lower_left_layout.addWidget(QLabel("Your gender:"))
        lower_left_layout.addWidget(self.genderBox)
        lower_left_layout.addWidget(QLabel("Your advantage:"))
        lower_left_layout.addWidget(self.advantageBox)
        lower_left_layout.addStretch(5)
        lower_left_layout.addWidget(self.btn)
        lower_left_widget.setLayout(lower_left_layout)
        
        lower_right_layout = QVBoxLayout()
        lower_right_layout.addWidget(self.textBox)
        lower_right_widget = QWidget()
        lower_right_widget.setLayout(lower_right_layout)

        lower_layout = QHBoxLayout()
        lower_layout.addWidget(lower_left_widget)
        lower_layout.addWidget(lower_right_widget)
        lower_layout.setStretch(0,1)
        lower_layout.setStretch(1,2)
        lower_widget = QWidget()
        lower_widget.setLayout(lower_layout)
        return lower_widget

    def praise_me(self):
        name = str(self.nameBox.text())
        gender = str(self.genderBox.currentText())
        advantage = str(self.advantageBox.currentText())

        sentence = [['怎么可以这么好！', '是要萌死我吗？', '举止端方，温文尔雅', '知书达理', '言谈可亲', '是我的小天使',\
                    '豁达开朗', '温柔体贴善解人意', '非常绅士', '为人大方，乐于助人', '重情重义', '是个值得信任的男人'], 
                    ['博闻强记', '才高八斗', '饱读诗书', '秀外慧中', '真是个小机灵鬼', '明明可以靠脸吃饭，非要靠才华',\
                    '品学兼优', '学富五车', '上知天文下知地理','是诸葛亮转世', '有颜又有才', '可以说是“上得厅堂，下得厨房”'],
                    ['好苗条哦！我好酸', '是我的梦中女神', '美丽大方', '刚一出来我还以为是刘亦菲', '好可爱，像洋娃娃', '的可爱值得我用一生来守护',\
                    '好帅！！我想给你生猴子', '可太帅了，我能爱一辈子', '帅气又迷人', '是酷酷男孩！', '有着大海般深邃的眼睛', '是个帅小伙']]

        if gender == 'all':
            column_start = 0
            column_stop = len(sentence[0])
        elif gender == 'female':
            column_start = 0
            column_stop = int(len(sentence[0])/2)
        elif gender == 'male':
            column_start = int(len(sentence[0])/2)
            column_stop = len(sentence[0])
        else:
            print('genderBox error')

        if advantage == 'all':
            row = random.randrange(0, len(sentence))
        elif advantage == 'character':
            row = 0
        elif advantage == 'intelligence':
            row = 1
        elif advantage == 'appearance':
            row = 2
        else:
            print('advantageBox error')

        praise_sentence = sentence[row][random.randrange(column_start, column_stop)]

        self.textBox.setText("{}{}".format(name, praise_sentence))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
