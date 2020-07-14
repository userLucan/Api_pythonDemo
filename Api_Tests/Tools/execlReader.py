#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-13 20:35
# @Author  : 刘开
import os
import xlrd

class ExeclReader():
    def __init__(self,fielname,sheet):
        self.filename = fielname
        self.sheet = sheet

    def get_execl_data(self):
        rseult = []
        #路径参数化
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))   #返回路径名称
        base_dir = base_dir.replace('\\','/')
        # 拼凑文件路径
        file_paht = base_dir + '/Data/' +self.filename

        #读取execl
        execl=xlrd.open_workbook(file_paht)
        #获取sheet页
        worksheet=execl.sheet_by_index(self.sheet)

#        读表头
        keys = []
        for header in range (worksheet.ncols):
            keys.append(worksheet.cell(0,header).value)

        # 获取行数
        nrows = worksheet.nrows
        # 获取值
        nlocs = worksheet.ncols

        #读表体
        for lens in range(1,nrows):
            tmp = {}
            #再把表头与表体的值对应起来
            for l in range(nlocs):
                tmp[keys[l]] = worksheet.cell(lens,l).value
            rseult.append(tmp)
        return rseult

if __name__ == '__main__':
    exe = ExeclReader('data.xlsx',0)
    print(exe.get_execl_data())