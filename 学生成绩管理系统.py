#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 11:08
# @Author  : Reconnect
# @File    : 学生成绩管理系统.py
# @Description: P89

class Test:
    a = 0
    b = 0

    def __init__(self):
        self.__c = 0


# 分数类
class Score:
    def __init__(self):
        self.s = 0.0

    def input(self):
        self.s = float(input("请输入分数(0~100):"))

    def output(self):
        print(self.s, end="\t")


# 课程类
class Subject:
    def __init__(self):
        self.subject = ""
        self.teacher = ""

    def input(self):
        self.subject = str(input("请输入课程名称:"))
        self.teacher = str(input("请输入任课教师:"))

    def output(self):
        print(self.subject, self.teacher)


class Student:
    def __init__(self, s):
        self.name = ""
        self.sum = 0
        self.grade = {}
        self.subject = s

    def input(self):
        self.name = str(input("请输入学生姓名:"))
        for i in self.subject:
            print(i.subject, "课程", end=":")
            s = Score()
            s.input()
            self.grade[i] = s

    def count(self):
        for i in self.subject:
            self.sum += self.grade[i].s

    def output(self):
        print(self.name, end=" ")
        for i in self.subject:
            self.grade[i].output()
        print(self.sum, end="\t")


def kc():
    print("***课程信息输入***")
    sub = []
    while True:
        subject = Subject()
        subject.input()
        if subject.subject == "**":
            break
        else:
            sub.append(subject)
    return sub


def cj(sub):
    print("***学生信息输入***")
    class_jd = []
    while True:
        stu = Student(sub)
        stu.input()
        stu.count()
        class_jd.append(stu)
        if input("继续(y/n)?") in ['n', 'N']:
            break
    return class_jd


def main():
    print("***学生成绩管理系统***")
    sub = kc()
    class_jd = cj(sub)
    class_jd.sort(key=lambda class_jd: class_jd.sum)
    print("***结果输出***")
    print("最高分是:", max(class_jd, key=lambda class_jd: class_jd.sum).sum)
    print("最低分是:", min(class_jd, key=lambda class_jd: class_jd.sum).sum)

    print("姓名", end="\t")
    for i in sub:
        print(i.subject, end="\t")
    print("总分")

    for i in class_jd:
        i.output()
        print()


if __name__ == '__main__':
    main()
