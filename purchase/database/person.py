"""
@ File Name     :   person.py
@ Time          :   2022/07/19
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   单人的类
@ Class List    :   Person -- 买房人
"""

from utils.compute import compute_target
from utils.convinput import convert_input


class Person:
    """买房人
    Self Args:
        name (str): 姓名
        income (str): 年收入
        deposit (str): 存款项
        invest (str): 年化投资收益
        target (str): 目标房首付金额
        time_year (float): 剩余总年数
        time_int_year (int): 剩余整年数
        time_month (int): 剩余月份
    """

    def __init__(self):
        """初始化"""

        self.name = None
        self.income = None
        self.deposit = None
        self.invest = None
        self.target = None
        self.time_year = None
        self.time_int_year = None
        self.time_month = None

    def get_base_info(self):
        """获取输入"""

        self.income = convert_input(input("请输入年收入（元）: "))
        self.deposit = convert_input(input("请输入存款项（元）: "))
        self.invest = convert_input(input("请输入年化投资收益（元）: "))
        self.target = convert_input(input("请输入目标房首付金额（元）: "))

    def compute_target(self):
        """计算结果"""

        self.time_year, self.time_int_year, self.time_month = compute_target(
            self.income, self.deposit, self.invest, self.target
        )

    def format_output(self):
        """输出"""

        print(
            "剩余年数: {}\n剩余{}年{}个月".format(
                self.time_year, self.time_int_year, self.time_month
            )
        )
