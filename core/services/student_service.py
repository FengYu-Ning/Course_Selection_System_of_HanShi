#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
import os,pickle
from conf import settings       # 导入文件路径
from core import identifier          # 导入主界面的模块
from core.services import admin_service
from lib import commons


def student_view():
    '''学生视图'''
    while True:
        print('''
\n************** 欢迎进入学生视图,请选择功能 **************
1.注册
2.登陆
3.返回上一级
4.退出程序        
''')
        cmd=input("请输入你的选择：").strip()

        if cmd == '1':
            admin_service.ZC_student()

        elif cmd == '2':
            while True:
                print("\n--------- 登陆 ---------\n(输入‘0’返回上一层)")
                name = input('请输入用户名： ')
                if name == "0":
                    return student_view()
                name_id = input('请输入用户ID： ')  # 登录，如果数据库中有对应文件，继续执行，否则打印用户不存在
                res = os.listdir(settings.STUDENT_DB_PATH)
                input_tag = False
                for i in res:
                    file_path = r'%s\%s' % (settings.STUDENT_DB_PATH,i)
                    with open(file_path, 'rb') as f:
                        student_obj = pickle.load(f)
                        if name == student_obj.name and name_id == student_obj.user_id:
                            print("登录成功。。。")
                            student_tag = True      # 判断 登录状态：True为 登录状态
                            input_tag = True
                            while student_tag:
                                print('''
\n------- 请选择功能 -------
1.查看个人信息
2.选择课程
3.退出登录
4.退出程序
                                ''')
                                cmd = input("请输入你的选择：").strip()

                                if cmd == '1':          # 查看个人信息
                                    student_obj.print_info()

                                elif cmd == '2':        # 选择课程
                                    choice_course =True
                                    res = os.listdir(settings.COURSE_DB_PATH)
                                    for item in res:
                                        file_path = r'%s\%s' % (settings.COURSE_DB_PATH, item)
                                        with open(file_path, 'rb') as f:
                                            course_obj = pickle.load(f)
                                            course_obj.print_info()
                                    while choice_course:
                                        course_cmd = input('请选择课程：').strip()
                                        for item in res:
                                            file_path = r'%s\%s' % (settings.COURSE_DB_PATH, item)
                                            with open(file_path, 'rb') as f:
                                                course_obj = pickle.load(f)
                                                if course_obj.course == course_cmd:
                                                    choice_course=False
                                                    if course_obj.student != []:
                                                        for i in course_obj.student:
                                                            if student_obj.name == i:
                                                                print('你已加入课程')
                                                                break
                                                            else:
                                                                course_obj.student.append(student_obj.name)
                                                                student_obj.student_course.append(course_obj.course)
                                                                student_obj.save()
                                                                course_obj.save()
                                                                print('选课成功')
                                                                break
                                                    else:
                                                        course_obj.student.append(student_obj.name)
                                                        student_obj.student_course = course_obj.course
                                                        student_obj.save()
                                                        course_obj.save()
                                                        print('选课成功')
                                                        break
                                                    break
                                        while choice_course:
                                            print("\n该课程不存在或输入错误")
                                            print("返回上一级请输入‘0’\n继续选课请输入任意非‘0’的字符")
                                            a = input().strip()
                                            if a == "0":
                                                break
                                        break
                                elif cmd == '3':
                                    student_tag = False
                                    print("成功退出。。。")
                                    return student_view()
                                elif cmd == '4':
                                    exit()
                                else:
                                    print("输入错误，请重新输入")
                if input_tag == False:
                    print('用户名或用户ID输入错误')
        elif cmd == '3':
            return identifier.func()
        elif cmd == '4':
            exit()
        else:continue



if __name__ == "__main__":
    student_view()

