"""
@ File Name     :   main.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   Hangman游戏
@ Function List :   main() -- 入口
@ Details       :   None
"""

import argparse

from runui import run_ui
from utils.setlog import LOGGER
from utils.inputbox import str2bool
from game.hangman import HangmanGamer


def main(config):
    """入口"""
    if config.isUI:
        run_ui()
    else:
        gamer = HangmanGamer("./data/hangman.txt")
        # print(gamer.word)
        gamer.start_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--isUI", type=str2bool, default=False)
    config = parser.parse_args()
    LOGGER.info("Start")
    main(config)
    LOGGER.info("Done")
