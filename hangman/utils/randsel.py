"""
@ File Name     :   randsel.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   随机生成一个数作为目标单词的序号
@ Function List :   rand_select() -- 生成一个随机整数
"""

import random
import time


def rand_select(length: int):
    """生成随机数

    Args:
        length (int): 总个数

    Returns:
        (int): 生成的随机数
    """
    random.seed(time.time())
    return random.randint(0, length - 1)
