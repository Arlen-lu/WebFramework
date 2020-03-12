import unittest
import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from PageObjects.login_page import LoginPage
from PageLocators.ele_locator import LoginLocators
from TestDatas import testlogin_datas
from selenium import webdriver
from TestDatas import common_datas
from ddt import ddt,data,unpack
from PageObjects.index_page import IndexPage
import warnings
import pytest
'''用来定义测试用例，只涉及业务顺序和判定断言结果是否为true'''
@ddt
class TestLogin(unittest.TestCase): #由于继承，父类中是存在初始化的值的，故，再继承的时候，需要对初始化的值进行处理
    '''
    1.进入登录页面
    2.输入账号-密码-点击登录
    3.断言是否成功
    '''

    def __init__(self,methodname = None):
        self.methodname = methodname
        super(TestLogin,self).__init__(self.methodname)

    @classmethod
    def setUpClass(cls):
        print("=========整个测试类只执行一次的前置============")
        cls.driver = webdriver.Firefox() #打开网页
        cls.driver.get(common_datas.home_url) #进入网址
        cls.driver.maximize_window()
        common_datas.window_handles_list = cls.driver.window_handles #将window_handles信息存入变量
        cls.lp = LoginPage(cls.driver) #PageObjects.login_page
        
        # driver = webdriver.Firefox()
        # cls.driver.get(common_datas.home_url)
    def setUp(self):
        #print("============类当中每一个测试用例都会执行的前置===============")
        warnings.simplefilter('ignore',ResourceWarning)
        print('test_begin!')
    #每次执行完一个测试用例，都需要刷新页面
    def tearDown(self):
        # print("============类当中每一个测试用例都会执行的后置===============")
        print('test_end!')
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=========整个测试类只执行一次的后置============")
        cls.driver.close()
        cls.driver.quit()

    #输入存在为空的情况
    #question!!!针对load导入的case，需要执行多次该用例，暂时无法run多次
    #改用ddt
    # test_data = testlogin_datas.login_fail_null
    @data(*(testlogin_datas.login_fail_null))
    def test_login_1_fail_null(self,test_data):
        self.lp.login(test_data['user_name'],test_data['user_pwd'])
        try:
            self.assertEqual(self.lp.get_null_msg(),test_data['msg'])
            self.lp.getlog.get_logging('INFO','Test Pass!')
        except Exception as e:
            self.lp.getlog.get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            raise e

    # 输入错误and无授权
    @data(*(testlogin_datas.login_fail_wrong))
    def test_login_2_fail_wrong(self,testdata):
        self.lp.login(testdata['user_name'],testdata['user_pwd'])
        self.assertEqual(self.lp.get_wrong_msg(),testdata['msg'])
        try:
            self.assertEqual(self.lp.get_wrong_msg(),testdata['msg'])
            self.lp.getlog.get_logging('INFO','Test Pass!')
        except Exception as e:
            self.lp.getlog.get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            raise e
    #成功
    #通过pytest打上标签，标注为冒烟的case之一
    # @pytest.mark.smoke
    def test_login_3_success(self):
        '''
        登录成功的case
        '''
        self.lp.login(testlogin_datas.login_success[0]['user_name'],testlogin_datas.login_success[0]['user_pwd'])
        # try:
        #     self.assertTrue(IndexPage(self.driver).user_info_visiable())
        #     print("Pass")
        #     self.lp.getlog.get_logging('INFO','Test Pass!')
        # except Exception as e:
        #     self.lp.getlog.get_logging('INFO','Test Fail!')
        #     raise e
        #切换窗口
        # self.lp.switch_new_window('new')
        try:
            self.assertEqual(IndexPage(self.driver,model = self.lp.model).get_user_info_text(),testlogin_datas.login_success[0]['msg'])
            print(self.lp.model)
            self.lp.getlog.get_logging('INFO','Test Pass!')
        except Exception as e:
            self.lp.getlog.get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            raise e

if __name__ == "__main__":
    unittest.main()
    # a = TestLogin()
    # a.test_login_3_success()