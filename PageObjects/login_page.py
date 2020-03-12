'''封装元素'''
import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageLocators.ele_locator import LoginLocators as loc
from TestDatas import testlogin_datas
from Common.BasePages import BasePage
class LoginPage(BasePage):

    def __init__(self,driver,getlog,model=None):
        super(LoginPage,self).__init__(getlog,model)
        self.driver = driver
        self.getlog = getlog
        self.model = model

    def login(self,user_name,user_pwd):
        '''
        1.等待账号输入框出现
        2.输入账号
        3.输入密码
        4.点击登录
        '''
        self.model = "登录页面-登录功能"
        self.input_text(loc.user_name,user_name)
        self.input_text(loc.user_pwd,user_pwd)
        self.click_element(loc.btn_login)

    def get_wrong_msg(self):
        '''
        登录失败的错误信息
        '''
        self.model = '登录页面-获取页面正中间错误信息'
        return self.get_text(loc.data_wrong)
    
    def get_null_msg(self):
        '''
        登录失败，输入存在空值的情况
        '''
        self.model = '登录页面-登陆区域错误信息'
        return self.get_text(loc.data_null)




if __name__ == "__main__":
    # print(LoginLocator().user_name)
    driver = webdriver.Firefox()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    LoginPage(driver).login_obj(LoginLocator().user_name).send_keys(testlogin_datas.login_success[0]['user_name'])
    LoginPage(driver).login_obj(LoginLocator().user_pwd).send_keys(testlogin_datas.login_success[0]['user_pwd'])
    # print(login_ele)