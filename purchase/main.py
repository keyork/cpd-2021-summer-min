"""
@ File Name     :   main.py
@ Time          :   2022/07/19
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   买房问题
@ Function List :   main() -- 入口
"""

import argparse

from database.db import PersonDB
from database.person import Person
from utils.inputbox import str2bool
from utils.setlog import LOGGER


def main(config):
    """入口

    Args:
        config (config): 配置参数
    """

    if config.isfile:
        person_db = PersonDB(config.source, config.target)
        person_db.from_file()
    else:
        person_1 = Person()
        person_1.get_base_info()
        person_1.compute_target()
        LOGGER.info("Result")
        person_1.format_output()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--isfile", type=str2bool, default=False)
    parser.add_argument("--source", type=str, default="./data/demo.csv")
    parser.add_argument("--target", type=str, default="./data/result.csv")
    config = parser.parse_args()
    LOGGER.info("Start")
    main(config)
    LOGGER.info("Done")
