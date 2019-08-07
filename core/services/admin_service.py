#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
import os,pickle
from conf import settings       # 导入文件路径
from lib import commons     # 导入类的模块
from core import identifier          # 导入主界面的模块


def ZC_student():
    '''注册学生信息'''
    while True:
        print('\n------- 欢迎注册 -------')
        name = input('name: ').strip()
        name_id = input('name_id: ').strip()  # 注册账号
        age = input('age: ').strip()
        sex = input('sex: ').strip()
        if not name:
            print('姓名、ID必填')
            continue
        elif not name_id:
            print('ID必填')
            continue
        break
    student_obj = commons.Student(name, name_id, age, sex)
    student_obj.save()

def ZC_teacher():
    '''注册老师信息'''
    while True:
        name = input('请输入教师姓名： ').strip()
        user_id = input('请输入教师ID： ').strip()
        age = input('请输入教师年龄： ').strip()
        sex = input('请输入教师性别： ').strip()
        if not name or not user_id:
            print('名字或ID不能为空')
            continue
        break
    teacher_obj = commons.Teacher(name, user_id, age, sex)
    teacher_obj.save()
    print('%s 老师的信息创建成功' % teacher_obj.name)

def get_school_obj():
    '''注册校区信息'''
    while True:
        print("请选择所属校区：\n"
              "1.东丽A校区\n"
              "2.东丽B校区\n"
              "3.东区校区")
        choice = input().strip()
        if choice == '1':
            school_obj = commons.School("东丽A", "文科楼")
        elif choice == '2':
            school_obj = commons.School("东丽B", "伟南楼")
        elif choice == '3':
            school_obj = commons.School("东区", "理科楼楼")
        else:
            continue
        break
    return school_obj

def print_message(PATH):
    '''打印信息'''
    res = os.listdir(PATH)
    for i in res:
        file_path = r'%s\%s' % (PATH, i)
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
            obj.print_info()

def set_course(teacher_obj):
    '''创建课程'''
    school_obj = get_school_obj()
    while True:
        course = input('请输入课程名字： ').strip()
        site = school_obj.site
        if not course or not site:
            print('输入错误')
            continue
        break
    course_obj = school_obj.set_course(course, site, teacher_obj.name)
    teacher_obj.teacher_class = course
    teacher_obj.save()
    course_obj.save()
    school_obj.save()
    print('%s课程创建成功' % course_obj.course)

def admin_viwe():
    '''管理员视图'''
    while True:
        print('''
\n**************** 欢迎进入管理员视图 *****************
1.登陆(用户名：FengYu，密码：ning)
2.返回上一级
3.退出程序        
        ''')
        choice=input("请输入你的选择：").strip()
        if choice == '1':
            while True:
                name=input('请输入用户名(输入‘0’返回上一级)： ')
                if name == "0":
                    break
                password=input('请输入密码： ')
                if name == 'FengYu' and password == 'ning':
                    print("登录成功。。。")
                    tag=True
                    while tag:
                        print('\n------- 请选择功能 -------')
                        cmd=input('1.创建教师信息\n'
                                  '2.读取所有教师信息\n'
                                  '3.创建学生信息\n'
                                  '4.读取所有学生信息\n'  
                                  '5.创建课程信息\n'
                                  '6.读取所有课程信息\n'    
                                  '7.退出登录\n'
                                  '8.退出选课系统\n'
                                  '请输入你的选择：')
                        if cmd == '1':
                            ZC_teacher()

                        elif cmd == '2':
                            print_message(settings.TEACHER_DB_PATH)

                        elif cmd == '3':
                            ZC_student()

                        elif cmd == '4':
                            print_message(settings.STUDENT_DB_PATH)

                        elif cmd == '5':
                            while True:
                                teacher_name = input('请输入教师名： ')
                                if teacher_name == "0":
                                    break
                                name_id = input('请输入教师ID： ')
                                res = os.listdir(settings.TEACHER_DB_PATH)
                                input_tag=False
                                for item in res:
                                    file_path = r'%s\%s' % (settings.TEACHER_DB_PATH, item)
                                    with open(file_path, 'rb') as f:
                                        teacher_obj = pickle.load(f)
                                        if teacher_name == teacher_obj.name and name_id == teacher_obj.user_id:
                                            input_tag=True
                                            set_course(teacher_obj)
                                if input_tag:
                                    print("课程创建成功")
                                    break
                                else:
                                    print("教师用户名或ID输入错误，请重新输入(输入‘0’返回上一级)")

                        elif cmd == '6':
                            print_message(settings.COURSE_DB_PATH)

                        elif cmd == '7':
                            tag=False

                        elif cmd == '8':
                            exit()

                        else:
                            continue
                else:
                    print('\n用户名或密码错误')
                    print("返回上一级请输入‘0’\n继续登录请输入任意非‘0’的字符")

        elif choice == '2':
            return identifier.func()

        elif choice == '3':
            exit()

        else:
            continue




if __name__ == "__main__":
    admin_viwe()

