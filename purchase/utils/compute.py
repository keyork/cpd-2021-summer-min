"""
@ File Name     :   compute.py
@ Time          :   2022/07/19
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   计算剩余时间
@ Function List :   compute_target() -- 计算数字
                    compute_target_pd() -- 计算pandas的数据格式
"""


from math import ceil


def compute_target(income, deposit, invest, target):
    """计算剩余时间(数字)

    Args:
        income (int/float): 年收入
        deposit (int/float): 存款项
        invest (int/float): 年化投资收益
        target (int/float): 目标房首付金额

    Returns:
        time_year (float): 剩余总年数
        time_int_year (int): 剩余整年数
        time_month (int): 剩余月份
    """

    time_year = max((target - deposit) / (income + invest), 0)
    time_int_year = int(time_year)
    time_month = ceil((time_year - time_int_year) * 12) + 1
    if time_month == 12:
        time_month = 0
        time_int_year += 1

    return time_year, time_int_year, time_month


def compute_target_pd(df):
    """计算剩余时间(pandas数据格式)

    Args:
        df (pandas.DataFrame): 源数据

    Returns:
        df (pandas.DataFrame): 计算完成后的数据
    """

    df["剩余年数"] = (df["目标房首付金额"] - df["年存款项"]) / (df["年收入"] + df["年化投资收益"])
    df["剩余年数"] = df["剩余年数"] * (df["剩余年数"] > 0)
    df["剩余整年数"] = df["剩余年数"].astype(int)
    df["剩余月份数"] = ((df["剩余年数"] - df["剩余整年数"]) * 12).astype(int) + 1
    df["剩余整年数"] += 1 * (df["剩余月份数"] == 12)
    df["剩余月份数"] *= 1 - 1 * (df["剩余月份数"] == 12)
    df["剩余月份数"] *= df["剩余年数"] > 0

    return df
