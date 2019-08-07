#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
import os,pickle
from conf import settings       # 导入文件路径
from core import identifier          # 导入主界面的模块
from core.services import admin_service


def teacher_view():
    '''教师视图'''
    while True:
        print("\n*************** 欢迎进入教师视图，请登录 ***************\n(输入‘0’返回上一层)")
        name = input('请输入用户名： ')
        if name == "0":
            return identifier.func()
        name_id = input('请输入用户ID： ')
        res = os.listdir(settings.TEACHER_DB_PATH)
        for item in res:
            file_path = r'%s\%s' % (settings.TEACHER_DB_PATH, item)
            with open(file_path, 'rb') as f:
                teacher_obj = pickle.load(f)
                if name == teacher_obj.name and name_id == teacher_obj.user_id:
                    print("登陆成功。。。")
                    taecher_tag=True
                    while taecher_tag:
                        print("\n------- 请选择功能 -------")
                        cmd=input('1.查看个人信息\n'
                                  '2.创建课程\n'
                                  '3.查看班级学员列表\n'
                                  '4.修改学员成绩\n'
                                  '5.返回上一级\n'
                                  '6.退出选课系统\n'
                                  '请选择功能： ').strip()

                        if cmd == '1':
                            teacher_obj.print_info()

                        elif cmd == '2':
                            admin_service.set_course(teacher_obj)

                        elif cmd == '3':
                            res = os.listdir(settings.COURSE_DB_PATH)
                            for item in res:
                                course_path=r'%s\%s' % (settings.COURSE_DB_PATH, item)
                                with open(course_path, 'rb') as f:
                                    course_obj = pickle.load(f)
                                    if teacher_obj.teacher_class == course_obj.course:
                                        print("班级成员有：%s" %course_obj.student)

                        elif cmd == '4':
                            while True:
                                name = input('请输入想要修改的学生姓名：').strip()
                                name_id = input('请输入学生id： ').strip()
                                while True:
                                    grade = input('请输入要修改的成绩： '.strip())
                                    if grade.isdigit():
                                        break
                                    else:
                                        print("成绩输入错误，请输入整型数据")
                                        continue
                                grade = int(grade)
                                res = os.listdir(settings.STUDENT_DB_PATH)
                                input_tag=False
                                for item in res:
                                    file_path = r'%s\%s' % (settings.STUDENT_DB_PATH, item)
                                    with open(file_path, 'rb') as f:
                                        student_obj = pickle.load(f)
                                        if name == student_obj.name and name_id == student_obj.user_id:
                                            input_tag=True
                                            student_obj.grade = grade
                                            print('%s 的成绩已修改为 %s' %(student_obj.name,grade))
                                            student_obj.save()
                                            student_obj.print_info()
                                if input_tag:
                                    break
                                else:
                                    print("学生名或学生ID输入错误，请重新输入（返回请输入‘0’）")
                                if name == "0":
                                    break
                        elif cmd == '5':
                            taecher_tag=False
                        elif cmd == '6':
                            exit()
                        else:
                            continue
                else:
                    print('用户名或密码错误')
                    print("返回上一级请输入‘0’\n继续登录请输入任意非‘0’的字符")
                    a = input().strip()
                    if a == "0":
                        return identifier.func()


if __name__ == "__main__":
    teacher_view()
