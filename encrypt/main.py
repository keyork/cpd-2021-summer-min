"""
@ File Name     :   main.py
@ Time          :   2022/07/22
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   主文件
@ Function List :   main() -- 入口
@ Details       :   进行加解密, 输出
"""


import argparse
from ende.endecryptor import EnDecryptor


def main(config):
    """入口

    Args:
        config (config): 配置参数
    """

    key = input("请输入密钥: ")
    data = config.data
    endecryptor = EnDecryptor(key, data)
    endecryptor.check_input()
    endecryptor.run_en_de()
    endecryptor.output()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="Hello World!")
    config = parser.parse_args()
    main(config)
