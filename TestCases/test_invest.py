import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from TestDatas import invest_datas
from PageObjects import invest_page
# from TestCases import test_login_new
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time

@pytest.mark.test
@pytest.mark.usefixtures('init_module')
@pytest.mark.usefixtures('init_index')
@pytest.mark.usefixtures('init_invest')
@pytest.mark.usefixtures('init_account')
class TestInvest(object):
    

    @pytest.mark.parametrize('test_data',invest_datas.invest_not_multiple_of_10)
    @pytest.mark.usefixtures('init_funcs')
    @pytest.mark.run(order=4)
    def test_invest_not_multiple_of_10(self,init_module,init_index,init_invest,init_account,test_data):
        init_index.invest_is_available().click()
        init_invest.input_invest_ammount(test_data['invest_ammount'])
        time.sleep(2)
        try:
            assert test_data['msg']==init_invest.get_invest_btn_text()
            # init_invest.getlog.get_logging('INFO','Test Pass！')
            init_module[1].get_logging('INFO','Test Pass！')
        except Exception as e:
            # init_invest.getlog.get_logging('ERROR','Test Fail！msg:{}'.format(e))
            init_module[1].get_logging('ERROR','Test Fail！msg:{}'.format(e))
            raise e
    
    @pytest.mark.parametrize('test_data',invest_datas.invest_wrong)
    @pytest.mark.usefixtures('init_funcs')
    @pytest.mark.run(order=5)
    def test_invest_fail(self,init_module,init_index,init_invest,init_account,test_data):
        init_invest.input_invest_ammount(test_data['invest_ammount'])
        init_invest.click_invest_btn()
        try:
            assert init_invest.get_popbox_text() ==test_data['msg']
            # init_invest.getlog.get_logging('INFO','Test Pass!')
            init_module[1].get_logging('INFO','Test Pass!')
        except Exception as e:
            # init_invest.getlog.get_logging('ERROR','Test Fail!,msg:{}'.format(e))
            init_module[1].get_logging('ERROR','Test Fail!,msg:{}'.format(e))
            raise e
        finally:
            time.sleep(2)
            init_invest.click_popbox_accept()
    
    @pytest.mark.parametrize('test_data',invest_datas.invest_success)
    @pytest.mark.usefixtures('init_funcs')
    @pytest.mark.run(order=6)
    def test_invest(self,init_module,init_index,init_invest,init_account,test_data):
        '''
        投标成功:
        前提:登录成功
        1.选择可投资得标的，点击[抢投]按钮
        2.输入投资金额
        3.点击[投标]按钮
        4.点击[查看并激活按钮]
        '''
        # init_index.invest_is_available().click()
        account_balance_before = init_invest.get_account_balance()
        init_invest.input_invest_ammount(test_data['invest_ammount'])
        init_invest.click_invest_btn()
        text = init_invest.get_invest_success()
        time.sleep(2)
        init_invest.click_invest_activate()
        try:
            assert float(init_account.get_available_balance()) == (float(account_balance_before)-test_data['invest_ammount']) and text ==test_data['msg']
            # init_invest.getlog.get_logging('INFO','Test Pass!')
            init_module[1].get_logging('INFO','Test Pass!')
        except Exception as e:
            # init_invest.getlog.get_logging('ERROR','Test Fail！msg:{}'.format(e))
            init_module[1].get_logging('ERROR','Test Fail!,msg:{}'.format(e))
            raise e


        