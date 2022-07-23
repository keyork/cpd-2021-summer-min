"""
@ File Name     :   io.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   输入输出接口
@ Function List :   output_set() -- 输出长度
                    input_str() -- 获取输入
"""


def output_set(data: set):
    """输出长度

    Args:
        data (set): 结果数据
    """
    print(len(data))


def input_str():
    """获取输入

    Returns:
        data (str): 字符串
    """
    data = input("请输入一个字符串: ")
    return data
