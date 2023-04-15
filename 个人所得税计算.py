#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/21 10:52
# @Author  : Reconnect
# @File    : 2.10个人所得税计算.py
# @Description: P53页题

print("----个人所得税计算----")
tax = {"姓名": [], "收入": [], "税率": [], "应交所得税": []}
while True:
    name = input("请输入姓名(-1结束输入):")
    income = float(input("请输入收入(-1结束输入):"))
    if name == '-1' or income == -1:
        break
    tax["姓名"].append(name)
    tax["收入"].append(income)

# 判断
for i in range(len(tax["姓名"])):
    if tax["收入"][i] > 80000:
        tax["税率"].append(45)
        tax["应交所得税"].append(tax["收入"][i] * 0.45 - 15160)
    elif tax["收入"][i] > 55000:
        tax["税率"].append(35)
        tax["应交所得税"].append(tax["收入"][i] * 0.35 - 7160)
    elif tax["收入"][i] > 35000:
        tax["税率"].append(30)
        tax["应交所得税"].append(tax["收入"][i] * 0.30 - 4410)
    elif tax["收入"][i] > 25000:
        tax["税率"].append(25)
        tax["应交所得税"].append(tax["收入"][i] * 0.25 - 2660)
    elif tax["收入"][i] > 12000:
        tax["税率"].append(20)
        tax["应交所得税"].append(tax["收入"][i] * 0.20 - 1410)
    elif tax["收入"][i] > 3000:
        tax["税率"].append(10)
        tax["应交所得税"].append(tax["收入"][i] * 0.10 - 210)
    else:
        tax["税率"].append(3)
        tax["应交所得税"].append(tax["收入"][i] * 0.03)


# 输出
print("姓名\t收入\t税率\t应交所得税")
for i in range(len(tax["姓名"])):
    # print("%-10s%-14.2f%-8.0f%-6.2f" % (tax["姓名"][i], tax["收入"][i], tax["税率"][i], tax["应交所得税"][i]))
    print("{}\t\t{}\t{}\t\t{}".format(tax["姓名"][i], tax["收入"][i], tax["税率"][i], tax["应交所得税"][i]))

