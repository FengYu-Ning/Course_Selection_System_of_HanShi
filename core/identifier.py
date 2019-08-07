#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
'''主逻辑函数模块'''
from lib import commons
from conf import settings
import pickle
import os
from core.services import admin_service         # 导入管理员的模块
from core.services import teacher_service       # 导入老师的模块
from core.services import student_service       # 导入学生的模块

def func():
    while True:
        print("""
\n**************** 欢迎进入韩师选课系统 **************** 
# 请选择你的身份：
1、学生
2、老师
3、管理员
4、退出选课系统
==>""")
        cmd = input().strip()
        if cmd == '1':
            student_service.student_view()
        elif cmd == '2':
            teacher_service.teacher_view()
        elif cmd == '3':
            admin_service.admin_viwe()
        elif cmd == '4':
            exit()
        else:
            print('输入错误，请重新输入！')
            continue


if __name__ == "__main__":
    func()

