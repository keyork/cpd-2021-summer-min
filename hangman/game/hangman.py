"""
@ File Name     :   hangman.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   游戏主体的类
@ Class List    :   HangmanGamer
@ Details       :   None
"""

from ntpath import join
from utils.randsel import rand_select
from utils.setlog import LOGGER


class HangmanGamer:
    """游戏
    Self Args:
        word (str): 目标单词
        word_len (int): 目标单词的长度
        guess (str): 猜测的词
        guess_log (list): 猜词历史
        wrong_step (int): 已经错的步数
        done (bool): 是否猜对
    """

    def __init__(self, source_path):
        """初始化

        Args:
            source_path (str): 词表文件的路径
        """

        with open(source_path, "r") as data:
            self.data = data.readlines()
        self.word = self.data[rand_select(len(self.data))].rstrip()
        self.word_len = len(self.word)
        self.guess = list("-" * self.word_len)
        self.guess_log = []
        self.wrong_step = 0
        self.done = False
        self.ui_interface = {
            "guess_word": "".join(self.guess),
            "is_done": False,
            "wrong_step": 0,
            "info_text": "",
            "info_mode": "warn",
            "is_win": True,
            "answer": self.word,
        }

    def start_game(self):
        """开始游戏

        开一个循环, 获取输入, 然后判断
        """

        while (not self.done) and self.wrong_step <= 6:

            guess_letter = input("请输入猜测的字母: ")
            self.judge(guess_letter)

    def ui_game_step(self, guess_letter):

        self.judge(guess_letter)

    def judge(self, guess):
        """判断

        Args:
            guess (str): 猜测的字母
        """

        # 先判断输入是否标准
        if len(guess) != 1:
            LOGGER.warning("请输入1个字母")

            self.ui_interface["info_mode"] = "warn"
            self.ui_interface["info_text"] = "请输入1个字母"

            return
        if guess in self.guess_log:
            LOGGER.warning("重复输入")

            self.ui_interface["info_mode"] = "warn"
            self.ui_interface["info_text"] = "重复输入"

            return

        self.guess_log.append(guess)

        if guess in self.word:
            # 猜对了
            for idx in range(self.word_len):
                if self.word[idx] == guess:
                    self.guess[idx] = guess
            LOGGER.info("字母在单词里")

            self.ui_interface["info_mode"] = "acc"
            self.ui_interface["info_text"] = "字母在单词里"
            self.ui_interface["guess_word"] = "".join(self.guess)

            print("".join(self.guess))
            if self.guess == list(self.word):
                self.done = True
                LOGGER.info("你赢了")
                LOGGER.info("结果: {}".format("".join(self.guess)))

                self.ui_interface["is_done"] = self.done
                self.ui_interface["is_win"] = True
        else:
            # 猜错了
            self.wrong_step += 1
            LOGGER.error("字母不在单词里")

            self.ui_interface["info_mode"] = "err"
            self.ui_interface["info_text"] = "字母不在单词里"
            self.ui_interface["wrong_step"] += 1

            print("".join(self.guess))
            if self.wrong_step == 7:
                self.done = True
                LOGGER.error("你输了")
                LOGGER.error("正确答案: {}".format(self.word))

                self.ui_interface["is_done"] = self.done
                self.ui_interface["is_win"] = False
