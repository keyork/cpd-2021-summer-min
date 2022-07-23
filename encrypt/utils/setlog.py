"""
@ File Name     :   setlog.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   控制台输出彩色log
@ Function List :   log_color() -- 彩色log
"""


import logging
import colorlog


def log_color():
    """彩色log

    Returns:
        color_logger (log): 封装变量
    """
    color_logger = logging.getLogger("ROOT")
    color_logger.setLevel(logging.DEBUG)

    log_handler = logging.StreamHandler()
    log_handler.setLevel(logging.DEBUG)

    fmt_str = "%(log_color)s[%(levelname)s]: %(message)s (%(asctime)s)"

    log_colors = {
        "DEBUG": "bg_blue",
        "INFO": "bg_green",
        "WARNING": "bg_yellow",
        "ERROR": "bg_red",
        "CRITICAL": "bg_purple",
    }

    the_format = colorlog.ColoredFormatter(fmt_str, log_colors=log_colors)
    log_handler.setFormatter(the_format)
    color_logger.addHandler(log_handler)

    return color_logger


LOGGER = log_color()
