"""
@ File Name     :   inputbox.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   使用argparse时解决bool型参数的问题
@ Function List :   str2bool() -- 将argparse获取的str转成bool
"""


import argparse


def str2bool(v: str):
    """将argparse获取的str转成bool

    Args:
        v (str): 输入的str参数

    Raises:
        argparse.ArgumentTypeError: 异常输入

    Returns:
        (bool): 转换后的bool
    """
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")
