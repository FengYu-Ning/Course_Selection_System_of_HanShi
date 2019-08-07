#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
'''程序起始位置'''
import sys,os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))   # 获取主文件夹路径
sys.path.append(BASE_PATH)   # 在环境变量中添加主文件夹路径，使得在子文件夹的.py文件能调用别的子文件夹的函数

from core import identifier     # 导入逻辑模块


if __name__ =='__main__':
    identifier.func()
