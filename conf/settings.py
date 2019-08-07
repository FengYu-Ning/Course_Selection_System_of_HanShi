#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
'''各个数据库的文件夹路径'''
import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))   # 获取主文件夹路径

SCHOOL_DB_PATH = os.path.join(BASE_PATH,'db','school')
TEACHER_DB_PATH = os.path.join(BASE_PATH,'db','teacher')
COURSE_DB_PATH = os.path.join(BASE_PATH,'db','courses')
STUDENT_DB_PATH = os.path.join(BASE_PATH,'db','student')




if __name__ == '__main__':
    print(SCHOOL_DB_PATH)

