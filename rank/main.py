"""
@ File Name     :   main.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   字符串排序输出
@ Function List :   main() -- 入口
"""


import argparse

from utils.inputbox import str2bool
from utils.io import input_str, output_set
from utils.setlog import LOGGER
from utils.sort import sort


def main(config):
    """入口

    Args:
        config (parse_args): 配置参数
    """
    data = input_str()
    result = sort(data, config)
    output_set(result)


if __name__ == "__main__":

    LOGGER.info("Start")

    parser = argparse.ArgumentParser()
    parser.add_argument("--sortout", type=str2bool, default=False)
    config = parser.parse_args()

    main(config)

    LOGGER.info("Done")
