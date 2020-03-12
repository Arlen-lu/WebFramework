import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
import unittest
from unittest.loader import TestLoader
from TestCases.test_login import TestLogin
import HTMLTestRunnerNew
from Common import dir_config
import time
import pytest
import pytest_reportlog
import pytest_html
# import pytest_rerunfailures
# import allure

# suit = unittest.TestSuite()
# loader = TestLoader()
# suit.addTest(loader.loadTestsFromTestCase(TestLogin))
# # runner = unittest.TextTestRunner()
# # runner.run(suit)
# # test_report = r"D:\python\mystudy\WebFramework\output\reports\test.html"
test_report = os.path.join(dir_config.reports_dir,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'-test_report.html')
test_log = os.path.join(dir_config.logs_dir,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'-test_log.json')
# with open(test_report,'wb+') as f:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(f,verbosity=2,title='web',description='web',tester='Arlen')
#     runner.run(suit)

# log_path = r'output\logs\log.txt'
# report_path = r'output\reports\test.html'
mark_name = 'test'
# a = '-m test --report-log'+'='+'output\\logs\\log.txt' ' --html' +'='+'output\\reports\\test.html'
# print(a)
text = '-m {} -q -s'.format(mark_name)
text1 = '--capture=no'
text_log = '--report-log={}'.format(test_log)
text_html = '--html={}'.format(test_report)
# print(text1)
pytest.main([text,text1,text_log,text_html])
# pytest.main(['-m','test','-q','-s','--report-log=output\logs\log.json','--alluredir','output\\report'])
