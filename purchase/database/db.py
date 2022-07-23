"""
@ File Name     :   db.py
@ Time          :   2022/07/19
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   文件数据库的类
@ Class List    :   PersonDB -- 文件数据库的类
"""

from utils.compute import compute_target_pd
from utils.fromfile import get_data_from_file


class PersonDB:
    """从文件读取的文件数据库
    Self Args:
        source_path (str): 源文件路径
        target_path (str): 输出文件路径
        db (pandas.DataFrame): 数据
    """

    def __init__(self, source_path, target_path):
        """初始化

        Args:
            source_path (str): 源文件路径
            target_path (str): 输出文件路径
        """
        self.source_path = source_path
        self.target_path = target_path
        self.db = None

    def from_file(self):
        """处理文件"""

        base_db = get_data_from_file(self.source_path)
        self.db = compute_target_pd(base_db)
        self.db.to_csv(self.target_path)
