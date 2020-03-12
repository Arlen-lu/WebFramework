import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageLocators.ele_locator import InvestLocators as loc
from Common.BasePages import BasePage
class InvestPage(BasePage):


    def __init__(self,driver,getlog,model=None):
        super(InvestPage,self).__init__(getlog,model)
        self.driver = driver
        self.model = model
        self.getlog = getlog
    #输入投资金额
    def input_invest_ammount(self,ammount):
        self.model ='投标功能:输入投标金额'
        self.input_text(loc.invest_input,ammount)
    #点击投标
    def click_invest_btn(self):
        self.model ='投标功能:点击投标'
        self.click_element(loc.invest_btn)
    #获取btn的text值
    def get_invest_btn_text(self):
        self.model ='投标功能:点击投标'
        return self.get_text(loc.invest_btn)
    #点击查看并激活按钮
    def click_invest_activate(self):
        self.model ='投标功能：查看并激活按钮'
        self.click_element(loc.invest_activate)
    #获取投标剩余金额
    def get_invest_balance(self):
        self.model ='投标功能：标的剩余金额'
        return self.get_text(loc.invest_balance)
    #获取账户余额
    def get_account_balance(self):
        self.model ='投标功能：账户剩余金额'
        return self.get_element_values(loc.invest_input,'data-amount')
    #获取弹出框的错误提示信息
    def get_popbox_text(self):
        self.model ='投标功能：弹出框错误提示'
        return self.get_text(loc.popbox_text)
    #点击弹出框的确认按钮
    def click_popbox_accept(self):
        self.model = '投标功能:确认弹出框错误提示'
        self.click_element(loc.popbox_accept)
    #获取投标成功标记
    def get_invest_success(self):
        self.model ='投标功能：投标成功'
        return self.get_text(loc.invest_success)
         
