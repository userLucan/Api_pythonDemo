#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-13 20:35
# @Author  : 刘开
import os
import xlrd

from Tools.logger import Logger
logger = Logger(logger='execl').getlog()

class ExeclReader():
    def __init__(self,fielname,sheet):
        self.filename = fielname
        self.sheet = sheet


    def get_execl_name(self):

        #路径参数化
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))   #返回路径名称
        base_dir = base_dir.replace('\\','/')
        # 拼凑文件路径
        file_paht = base_dir + '/Data/' +self.filename
        logger.info('开始查找文件')

        #读取execl
        execl=xlrd.open_workbook(file_paht)
        #获取sheet页
        worksheet=execl.sheet_by_name(self.sheet)
        logger.info('通过sheet名称读取文件内容')
#        读表头
        keys = []
        for header in range (worksheet.ncols):
            keys.append(worksheet.cell(0,header).value)
        logger.info('读取execl表头信息')
        # 获取行数
        nrows = worksheet.nrows
        logger.info('读取execl行数')
        # 获取值
        nlocs = worksheet.ncols
        logger.info('获取行数里面的值')
        rseult = []
        #读表体
        for lens in range(1,nrows):
            tmp = {}
            #再把表头与表体的值对应起来
            for response in range(nlocs):
                 tmp[keys[response]] = worksheet.cell(lens,response).value
            rseult.append(tmp)
        return rseult
    logger.info('把表头与内容以键值对的方式读取出来')

    def get_execl_index(self):

        # 路径参数化
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))  # 返回路径名称
        base_dir = base_dir.replace('\\', '/')
        # 拼凑文件路径
        file_paht = base_dir + '/Data/' + self.filename
        logger.info('11111111111111')

        # 读取execl
        execl = xlrd.open_workbook(file_paht)
        # 获取sheet页
        worksheet = execl.sheet_by_index(self.sheet)
        logger.info('22222222222222222')
        #        读表头
        keys = []
        for header in range(worksheet.ncols):
            keys.append(worksheet.cell(0, header).value)
        logger.info('3333333333333')
        # 获取行数
        nrows = worksheet.nrows
        logger.info('444444444444')
        # 获取值
        nlocs = worksheet.ncols
        logger.info('555555555')
        rseult = []
        # 读表体
        for lens in range(1, nrows):
            tmp = {}
            # 再把表头与表体的值对应起来
            for response in range(nlocs):
                tmp[keys[response]] = worksheet.cell(lens, response).value
            rseult.append(tmp)
        return rseult
if __name__ == '__main__':
    exe = ExeclReader('global_analysis.xlsx','实时分析')
    res=exe.get_execl_name()
    print(res)
    for ress in res:
        print(type(ress))
        print(ress['id'])


    # print(res[0])
    # sss=res[0]
    # for eee in sss.values():

        # aser.append(eee.get('id'),
        #             eee.get('method'))
        # for data in datas.values():
        #     asser = []
        #     asser.append((data.get("url"),
        #                   data.get("key"),
        #                   data.get("start_code"),
        #                   data.get("error_code")))
        # return asser

