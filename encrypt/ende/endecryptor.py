"""
@ File Name     :   endecryptor.py
@ Time          :   2022/07/22
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   加密解密的类
@ Class List    :   EnDecryptor -- 加解密的类
@ Details       :   加密解密
"""

from utils.setlog import LOGGER


class EnDecryptor:
    """加解密
    Self Args:
        key (int): 密钥
        raw_data (str): 原数据
        encr_data (str): 加密后的数据
        decr_data (str): 解密后的数据
    """

    def __init__(self, key, raw_data):
        """初始化

        Args:
            key (int): 密钥
            raw_data (str): 原数据
        """

        self.key = key
        self.raw_data = raw_data
        self.encr_data = None
        self.decr_data = None

    def check_input(self):
        """检查密钥格式

        验证是否为正整数, 并将范围控制在0~25, 便于后续计算
        """

        while True:
            try:
                self.key = int(self.key)
                if self.key % 1 == 0 and self.key > 0:
                    LOGGER.info("Key验证通过")
                    break
                else:
                    LOGGER.error("Key数字错误")
                    self.key = input("请重新输入加密Key: ")
            except:
                LOGGER.error("Key格式错误")
                self.key = input("请重新输入加密Key: ")

        self.key = self.key % 26

    def process_letter(self, is_encr, letter):
        """对单个字母进行加解密

        Args:
            is_encr (bool): 是否加密, 若为False则为解密
            letter (str): 待处理的字母

        Returns:
            letter (str): 处理后的字母
        """

        if is_encr:
            if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
                # 小写字母
                letter = chr((ord(letter) - ord("a") + self.key) % 26 + ord("a"))
            elif ord(letter) >= ord("A") and ord(letter) <= ord("Z"):
                # 大写字母
                letter = chr((ord(letter) - ord("A") + self.key) % 26 + ord("A"))
        else:
            if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
                # 小写字母
                letter = chr((ord(letter) - ord("a") - self.key + 26) % 26 + ord("a"))
            elif ord(letter) >= ord("A") and ord(letter) <= ord("Z"):
                # 大写字母
                letter = chr((ord(letter) - ord("A") - self.key + 26) % 26 + ord("A"))
        return letter

    def encrypt(self):
        """加密"""
        LOGGER.info("进行加密")
        data = list(self.raw_data)
        for idx in range(len(data)):
            data[idx] = self.process_letter(True, data[idx])
        self.encr_data = "".join(data)

    def decrypt(self):
        """解密"""
        LOGGER.info("进行解密")
        data = list(self.raw_data)
        for letter in data:
            self.process_letter(False, letter)
        self.decr_data = "".join(data)

    def run_en_de(self):
        """封装加解密"""
        self.encrypt()
        self.decrypt()

    def output(self):
        """输出"""
        print("加密后: {}".format(self.encr_data))
        print("解密后: {}".format(self.decr_data))
        print("原数据: {}".format(self.raw_data))
