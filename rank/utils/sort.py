"""
@ File Name     :   sort.py
@ Time          :   2022/07/20
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   排序算法, 递归
@ Function List :   sort_part() -- 递归函数排序
                    sort() -- 调用排序
"""

from utils.igncase import ignore_case, recover_case


def sort_part(data: list, length: int, result: list, sorted: int):
    """递归函数排序

    Args:
        data (list): 列表数据
        length (int): 列表长度
        result (list): 排序结果
        sorted (int): 排序起始位置
    """
    if sorted == length - 1:
        result = result.append("".join(data.copy()))
        print("".join(data.copy()))
    else:
        for idx in range(sorted, length):
            data[sorted], data[idx] = data[idx], data[sorted]
            sort_part(data, length, result, sorted + 1)
            data[sorted], data[idx] = data[idx], data[sorted]


def sort(data: str, config):
    """调用排序

    Args:
        data (str): 数据
        config (config): 配置参数

    Returns:
        set(result) (set): 排序结果
    """
    data_list = list(data)
    if config.sortout:
        temp_list = ignore_case(data_list.copy())
        temp_list.sort()
        data_list = recover_case(temp_list.copy())
    length = len(data_list)
    result = []
    sorted = 0
    sort_part(data_list, length, result, sorted)
    return set(result)
