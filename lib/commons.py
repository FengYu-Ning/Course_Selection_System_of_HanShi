#!/usr/bin/env python
# -*- coding:utf8 -*-
# by LZN
'''各个类的模块'''
from conf import settings
import pickle

class School:
    '''校区与地点'''
    def __init__(self,area,site):
        self.area=area
        self.site=site
        self.area_courses=[]    # 创建一个空列表存放课程
        self.area_teacher=[]    # 创建一个空列表存放老师

    def set_course(self,course,site,teacher):
        '''创建课程'''
        course_obj=Course(course,site,teacher)
        self.area_courses.append(course_obj)
        return course_obj

    def set_teacher(self,name,user_id,age,sex):
        '''创建老师'''
        teacher_obj=Teacher(name,user_id,age,sex)
        self.area_teacher.append(teacher_obj)
        return teacher_obj

    def save(self):
        '''保存校区文件信息'''
        with open(r'%s\%s' %(settings.SCHOOL_DB_PATH,self.area),'wb') as f:
            pickle.dump(self,f)
            f.flush()

class Course:
    '''课程类'''
    def __init__(self,course,site,teacher):
        self.course=course
        self.site=site
        self.teacher=teacher
        self.student=[]     # 为学生创建空列表

    def print_info(self):
        '''查看课程信息'''
        print('''
\n-------- 课程信息 ---------
课程名：%s
授课老师：%s
上课地点：%s
学生：%s
        ''' %(self.course,self.teacher,self.site,self.student))

    def save(self):
        '''保存课程信息'''
        with open(r'%s\%s' %(settings.COURSE_DB_PATH,self.course),'wb') as f:
            pickle.dump(self,f)
            f.flush()


class People:
    def __init__(self,name,user_id,age,sex):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(People):
    def __init__(self,name,user_id,age,sex):
        People.__init__(self,name,user_id,age,sex)
        self.teacher_class=[]

    def print_info(self):
        '''查看老师信息'''
        print('''
\n--------教师信息---------
姓名:%s
ID:%s
年龄:%s
性别:%s
所教课程:%s
        ''' %(self.name,self.user_id,self.age,self.sex,self.teacher_class))

    def save(self):
        '''保存老师信息'''
        with open(r'%s\%s' % (settings.TEACHER_DB_PATH, self.name), 'wb') as f:
            pickle.dump(self, f)
            f.flush()

class Student(People):
    def __init__(self,name,user_id,age,sex):
        People.__init__(self,name,user_id,age,sex)
        self.student_course=[]
        self.grade=0

    def __str__(self):
        return self.name
    def print_info(self):
        '''查看学生信息'''
        print('''
\n---------学生信息----------
姓名:%s
ID:%s
年龄:%s
性别:%s
所报课程:%s
课程成绩:%s
        ''' %(self.name,self.user_id,self.age,self.sex,self.student_course,self.grade))

    def save(self):
        '''保存学生信息'''
        with open(r'%s\%s' %(settings.STUDENT_DB_PATH,self.name),'wb') as f:
            pickle.dump(self,f)
            f.flush()




if __name__ == '__main__':
    s1=Student('alex',"aujhsdfyga",'18','boy')
    s1.print_info()
    S1=School("东丽A","文科楼")
    print(S1.__dict__)
    t1=Teacher("tom","asdasf","30","girl")
    t1.print_info()
    print(s1)

