"""
@ File Name     :   igncase.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   处理大小写
@ Function List :   ignore_case() -- 将字母转成ascii码, 大写进行特殊处理
                    recover_case() -- 排序后将数字恢复成字母
@ Details       :   采用list.sort()函数进行排序, 对于字母则是根据ascii码进行排序
                    所以将小写字母转换成ascii码, 大写字母转换成对应小写字母的ascii码+0.5
                    +0.5的目的是便于将排序后的ascii码列表恢复成字母形式, 否则无法判断大小写
"""


def ignore_case(data: list):
    """将字母转成ascii码, 大写进行特殊处理

    Args:
        data (list): 原列表

    Returns:
        result (list): 处理后的列表
    """

    result = []
    for item in data:
        ascii_data = ord(item)
        if ascii_data >= 97:
            ascii_data -= 31.5
        result.append(ascii_data)
    return result


def recover_case(data: list):
    """将排序后的列表转回字母

    Args:
        data (list): 原列表

    Returns:
        result (list): 处理后的列表
    """

    result = []
    for item in data:
        if item % 1 == 0.5:
            item += 31.5
        result.append(chr(int(item)))
    return result
