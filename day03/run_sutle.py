"""
    目标：
    1、搜索组装测试套件
    2、运行测试套件并生成报告
"""
import HTMLTestRunner
import unittest
import time
from case.test_Gps_coordinate import GpsCoordinte
#组装测试套件
suite = unittest.defaultTestLoader.discover("./case/",pattern="test*.py")
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(GpsCoordinte))
#   指定报告存放路径以及文件名称
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d_%H%M%S"))
#运行测试套件并生成报告
with open(file_path,"wb") as f:
   HTMLTestRunner.HTMLTestRunner(stream = f,title="测试报告",description="测试结果详细信息").run(suite)
#





# case_path = './case'
# def get_allcase():
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="test_Gps_coordinate.py")
#     testsuite = unittest.TestSuite()
#     testsuite.addTest(discover)
#     return testsuite
#
# if __name__ == "__main__":
#     now = time.strftime("%Y%m%d_%H%M%S")
#     filename = './report/' + now + '11.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp, title='automation report', description='case execution status')
#     runner.run(get_allcase())
#     fp.close()
