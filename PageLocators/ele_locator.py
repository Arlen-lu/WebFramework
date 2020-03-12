'''封装元素定位'''
from selenium.webdriver.common.by import By

class LoginLocators(object):

    user_name = (By.XPATH,"//input[@name='phone']")
    user_pwd =(By.XPATH,"//input[@name='password']")
    btn_login = (By.CLASS_NAME,'btn-special')
    data_null = (By.CLASS_NAME,'form-error-info')
    data_wrong = (By.CLASS_NAME,'layui-layer-content')

#login_page.py文件里面使用 driver.find_element(*user_input)

class IndexLocators(object):
    #账号显示的名称
    user_info = (By.XPATH,"//a[@href = '/Member/index.html']")
    #投标标的
    invest_units = (By.XPATH,"//div[@class='b-unit']")
    #投标按钮
    invest_btns = (By.XPATH,"//div[@class='b-unit']//a[@class ='btn btn-special']")

class AccountLocators(object):
    #用户可用余额
    available_balance = (By.XPATH,"//div[@class='per_info_ct_left']//li[@class='color_sub']")
    #账号显示名称
    regname =(By.XPATH,"//span[@class='regname']")

class InvestLocators(object):
    #标的剩余额度
    invest_balance = (By.XPATH,"//span[contains(text(),'剩余')]/following-sibling::span[1]")
    #账户可用余额+输入框
    invest_input = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")
    #投标按钮(输入不为10的倍数时，错误提示为该text值)
    invest_btn = (By.XPATH,"//button[contains(@class,'btn-special')]")
    #错误提示的弹出框
    popbox_text =(By.XPATH,"//div[contains(@class,'layui-layer-content')]/div[@class='text-center']")
    #错误弹出框的确定按钮
    popbox_accept =(By.XPATH,"//div[@id='layui-layer1']//a[text()='确认']")
    #投标成功表制
    invest_success = (By.XPATH,"//div[@class='layui-layer-content']//div[text()='投标成功！']")
    #查看并激活
    invest_activate = (By.XPATH,"//div[@class='layui-layer-content']//button[text()='查看并激活']")

