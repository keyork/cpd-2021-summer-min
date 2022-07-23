import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
from ui.singlemodeui import Ui_MainWindow
from game.hangman import HangmanGamer


class SingleModelGame(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SingleModelGame, self).__init__(parent)
        self.setupUi(self)

        self.judge_font = QFont()
        self.judge_font.setPointSize(48)
        self.answer_font = QFont()
        self.answer_font.setPointSize(24)
        self.info_font = QFont()
        self.info_font.setPointSize(24)

        self.gamer = HangmanGamer("./data/hangman.txt")
        print(self.gamer.word)
        self.letterEdit.setPlaceholderText("请输入字母")
        self.exitButton.clicked.connect(self.close)
        self.confirmButton.clicked.connect(self.get_input)
        self.confirmButton.setShortcut(Qt.Key_Return)

    def get_input(self):
        input_letter = self.letterEdit.text()
        self.gamer.ui_game_step(input_letter)
        self.resultBrowser.setFontPointSize(24)
        self.resultBrowser.setText(self.gamer.ui_interface["guess_word"])
        self.show_info()
        self.judge_end()
        self.letterEdit.clear()
        self.letterEdit.setPlaceholderText("请输入字母")

    def show_info(self):
        self.infoLabel.setText(self.gamer.ui_interface["info_text"])
        self.infoLabel.setFont(self.info_font)
        if self.gamer.ui_interface["info_mode"] == "warn":
            self.infoLabel.setStyleSheet("color:orange")
        elif self.gamer.ui_interface["info_mode"] == "err":
            self.infoLabel.setStyleSheet("color:red")
        elif self.gamer.ui_interface["info_mode"] == "acc":
            self.infoLabel.setStyleSheet("color:green")

    def judge_end(self):

        if self.gamer.ui_interface["is_done"]:

            self.letterEdit.setDisabled(True)
            self.confirmButton.setDisabled(True)
            if self.gamer.ui_interface["is_win"]:
                self.judgeLabel.setText("你赢了")
                self.answerLabel.setText(self.gamer.ui_interface["answer"])
                self.judgeLabel.setFont(self.judge_font)
                self.answerLabel.setFont(self.answer_font)
                self.judgeLabel.setStyleSheet("color:green")
                self.answerLabel.setStyleSheet("color:green")
                self.resultBrowser.setStyleSheet("color:green")
            else:
                self.judgeLabel.setText("你输了")
                self.answerLabel.setText(self.gamer.ui_interface["answer"])
                self.judgeLabel.setFont(self.judge_font)
                self.answerLabel.setFont(self.answer_font)
                self.judgeLabel.setStyleSheet("color:red")
                self.answerLabel.setStyleSheet("color:red")
                self.resultBrowser.setStyleSheet("color:red")


def run_ui():
    app = QApplication(sys.argv)
    single_model = SingleModelGame()
    single_model.show()
    sys.exit(app.exec_())
