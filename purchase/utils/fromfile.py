"""
@ File Name     :   fromfile.py
@ Time          :   2022/07/19
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   从文件读取数据
@ Function List :   get_data_from_file() -- 读取文件, 返回数据
"""

import pandas as pd


def get_data_from_file(source_file: str):
    """读取文件

    Args:
        source_file (str): 文件路径

    Returns:
        raw_data (pandas.DataFrame): 数据
    """
    if source_file.endswith(".csv"):
        raw_data = pd.read_csv(source_file)
    elif source_file.endswith(".xlsx"):
        raw_data = pd.read_excel(source_file)
    return raw_data
