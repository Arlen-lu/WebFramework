import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
# from PageObjects.login_page import LoginPage
from TestDatas import testlogin_datas
from selenium import webdriver
# from TestDatas import common_datas
from PageObjects.index_page import IndexPage
import warnings
import pytest
# import pytest_reportlog
'''用来定义测试用例，只涉及业务顺序和判定断言结果是否为true'''
@pytest.mark.test
@pytest.mark.usefixtures('init_module')
@pytest.mark.usefixtures('init_login')
class TestLogin(object):
    '''
    1.进入登录页面
    2.输入账号-密码-点击登录
    3.断言是否成功
    '''
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures('init_funcs')
    @pytest.mark.parametrize('testdata',testlogin_datas.login_fail_null)
    def test_login_1_fail_null(self,init_module,init_login,testdata):
        init_login.login(testdata['user_name'],testdata['user_pwd'])
        try:
            assert init_login.get_null_msg()==testdata['msg']
            # init_login.getlog.get_logging('INFO','Test Pass!')
            init_module[1].get_logging('INFO','Test Pass!')
        except Exception as e:
            # init_login.getlog.get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            init_module[1].get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            raise e

    # 输入错误and无授权
    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures('init_funcs')
    @pytest.mark.parametrize('testdata',testlogin_datas.login_fail_wrong)
    def test_login_2_fail_wrong(self,init_module,init_login,testdata):
        init_login.login(testdata['user_name'],testdata['user_pwd'])
        try:
            assert init_login.get_wrong_msg()==testdata['msg']
            # init_login.getlog.get_logging('INFO','Test Pass!')
            init_module[1].get_logging('INFO','Test Pass!')
        except Exception as e:
            # init_login.getlog.get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            init_module[1].get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            raise e
    #成功
    #通过pytest打上标签，标注为冒烟的case之一
    # @pytest.mark.smoke
    @pytest.mark.run(order=3)
    # @pytest.mark.usefixtures('init_module')
    # @pytest.mark.usefixtures('init_login')
    @pytest.mark.usefixtures('init_funcs')
    @pytest.mark.test1
    def test_login_3_success(self,init_module,init_login):
        '''
        登录成功的case
        '''
        init_module[1].get_logging('INFO','测试成功的用例！')
        init_login.login(testlogin_datas.login_success[0]['user_name'],testlogin_datas.login_success[0]['user_pwd'])
        try:
            assert (IndexPage(init_module[0],init_module[1],model = init_login.model).get_user_info_text() == testlogin_datas.login_success[0]['msg'])
            print(init_login.model)
            # init_login.getlog.get_logging('INFO','Test Pass!')
            init_module[1].get_logging('INFO','Test Pass!')
        except Exception as e:
            # init_login.getlog.get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            init_module[1].get_logging('INFO','Test Fail!,msg:{0}'.format(e))
            raise e
        # try:
        #     self.assertTrue(IndexPage(self.driver).user_info_visiable())
        #     print("Pass")
        #     self.lp.getlog.get_logging('INFO','Test Pass!')
        # except Exception as e:
        #     self.lp.getlog.get_logging('INFO','Test Fail!')
        #     raise e
        #切换窗口
        # self.lp.switch_new_window('new')
        

if __name__ == "__main__":
    unittest.main()
    # a = TestLogin()
    # a.test_login_3_success()``