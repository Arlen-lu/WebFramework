'''
封装页面元素
'''
import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageLocators.ele_locator import IndexLocators as loc
from TestDatas import testlogin_datas
from Common.BasePages import BasePage

class IndexPage(BasePage):

    def __init__(self,driver,getlog,model=None):
        super(IndexPage,self).__init__(getlog,model)
        self.driver = driver
        self.getlog = getlog
        self.model = model

    def user_info_visiable(self):
        #用作判定登录成功
        self.model = '投标功能-账号名称'
        try:
            self.wait_visible(loc.user_info)
            return True
        except Exception as e:
            return False
    
    def get_user_info_text(self):
        self.model = '投标功能-获取账号名称'
        print('get_user_info_text：',self.model)
        return self.get_text(loc.user_info)
    #获取投标标的列表
    def get_invest_units(self):
        self.model = '投标功能-投标标的列表'
        return self.get_elements(loc.invest_units)
    #获取标的的投标按钮
    def get_invest_btns(self):
        self.model = '投标功能-获取投标按钮'
        return self.get_elements(loc.invest_btns)
    #判定标的是否可投标---投标按钮是否可点击
    def invest_is_available(self):
        self.model = '投标功能-投标按钮'
        invests= self.get_invest_btns()
        for i in range(len(invests)):
            if self.get_btn_is_clickable(invests[i]):
                return invests[i]
                break
            elif i==len(invests)-1 and self.get_btn_is_clickable(i)== False:
                return False
            else:
                continue

        