# 小作业 1-1

## 题目

买房问题：自主假设某人在 2022 年的月税后收入、月消费总额、月存款总额、月投资平均收益、目标房首付款等参数（参数个数不限），计算此人在某年某月可以凑够首付款。

具体要求

1. 从键盘输入年收入、年存款项、年化投资收益、目标房首付金额，以回车键或空格键作为输入结束标志。最后一个输入结束后，程序自动显示计算结果；
2. 输入和输出要有适当的文字提示；
3. 附加任务（供参考选做）：处理带有汉字的输入内容；从文件导入多个用户的状况进行批量计算并将计算结果保存到新文件;计算结果非整年时，将结果精度近似到月份。

## 环境

```bash
python==3.7
colorlog==6.6.0
openpyxl==3.0.10
pandas==1.3.5
```

## 运行方式

```bash
python main.py --isfile False
or
python main.py --isfile True --source './data/demo.csv' --target './data/result.csv'
```

参数说明

- `isfile`(True/False): 是否从文件中读取
- `source`(Path Str): 源文件
- `target`(Path Str): 结果文件

## 程序结构

```
purchase/   # 房价问题（小作业1-1）
├── main.py     # 入口
├── data/       # 数据和结果文件
├── database/   # 定义的数据类
│   ├── person.py   # 单人
│   ├── db.py   # 从文件读取
├── utils/      # 工具
│   ├── compute.py  # 计算剩余时间
│   ├── convinput.py    # 输入转换
│   ├── fromfile.py     # 从文件读取
│   ├── inputbox.py     # 输入bool的转换
│   ├── setlog.py       # 彩色log
```

## Log

- [x] 完成基础功能
- [x] 添加非整年近似
- [x] 添加从文件导入
- [ ] 添加处理汉字
- [ ] 格式化输入输出
- [ ] 图形界面
