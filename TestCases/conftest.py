'''
fixture文件
'''
import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from selenium import webdriver
from TestDatas import common_datas
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.invest_page import InvestPage
from PageObjects.account_page import AccountPage
from Common.getlogging import GetLogging
import time

import pytest
#添加自定义标签，解决pytest不识别标签名，导致标签不生效
def pytest_configure(config):
    mark_list = ['test','smoke','test1']
    for markers in mark_list:
        config.addinivalue_line(
            "markers", markers
        )

@pytest.fixture(scope='session')
def init_module():
    print("================配置测试类前提=======")
    getlogging = GetLogging()
    driver = webdriver.Chrome()
    driver.get(common_datas.home_url)
    driver.maximize_window()
    common_datas.window_handles_list = driver.window_handles
    getlogging.get_logging('INFO','测试开始！')
    yield [driver,getlogging]
    print("================配置测试类后置=======")
    driver.close()
    driver.quit()

@pytest.fixture(scope='class')
def init_login(init_module):
    # driver = init_module[0]
    login_p = LoginPage(*init_module)
    yield login_p

@pytest.fixture(scope='class')
def init_index(init_module):
    # driver = init_module[0]
    index_p = IndexPage(init_module[0],init_module[1])
    yield index_p
    
@pytest.fixture(scope='class')
def init_invest(init_module):
    # driver = init_module[0]
    invest_p = InvestPage(*init_module)
    yield invest_p

@pytest.fixture(scope='class')
def init_account(init_module):
    # driver = init_module[0]
    account_p = AccountPage(*init_module)
    yield account_p


@pytest.fixture(scope='function')
def init_funcs(init_module):
    driver = init_module[0]
    print("Test begin!")
    yield
    driver.refresh()
    print("Test End!")

