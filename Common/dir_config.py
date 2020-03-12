import os

#项目目录
base_dir= os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# base_dir2 = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
testdatas_dir = os.path.join(base_dir,'TestDatas')
testcases_dir = os.path.join(base_dir,'TestCases')
screenshot_dir = os.path.join(base_dir,'output\\imgs')
reports_dir = os.path.join(base_dir,'output\\reports')
logs_dir = os.path.join(base_dir,'output\\logs')
