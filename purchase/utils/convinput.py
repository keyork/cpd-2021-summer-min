"""
@ File Name     :   convinput.py
@ Time          :   2022/07/19
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   转换输入
@ Function List :   convert_input() -- 处理输入中的文字
"""


def convert_input(data: str):
    """处理输入中的文字

    Args:
        data (str): 输入的字符串

    Returns:
        output (float) / 0: 转换后的数字
    """
    try:
        output = float(data)
        return output
    except:
        print("输入中有字符串")
        return 0
