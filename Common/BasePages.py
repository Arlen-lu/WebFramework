'''
1.生成执行日志：测试用例的执行日志
2.测试用例的认合一行代码失败，都可再日志中看到异常信息，并生成失败的网页截图
3.精简PageObjects页面：
测试用例 = 页面对象（步骤+断言） + 测试手机壳i
页面对象 = 页面行为+页面元素定位
页面行为 =selenium webdriver的基本API操作
对webdriver的基础函数封装，加入日志，异常处理，失败截图

封装操作：输入，点击，清除
获取文本内容，获取元素属性
截图
iframe切换
window切换
等待元素可见
查找元素
为这些基础操作，添加log
'''
import os
import sys
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from selenium import webdriver
#显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from PageLocators.ele_locator import LoginLocator
from Common import dir_config
# from Common.getlog.get_logging import GetLogging
import time
from TestDatas import common_datas

class BasePage(object):
    def __init__(self,driver,getlog,model=None):
        self.driver = driver
        self.getlog = getlog
        self.model = model

    #等待元素可见
    def wait_visible(self,loc,timeout=30,poll_frequency=0.5):
        """
        :param loc: 元素定位表达。元组类型，表达方式(元素定位类型，元素定位方法)
        :param timeout: 等待上限。
        :param poll_frequency: 轮询频率
        :param model: 等待失败时，截图操作，图片文件中需要表达的功能模块标注。
        :return: None
        """
        try:
            start =time.time()
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(loc))
            end = time.time()
            self.getlog.get_logging('INFO','{0}:元素{1}已出现，等待时长{2}s'.format(self.model,loc,(end-start)))
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:等待元素{1}失败,msg:{2}'.format(self.model,loc,e))
            self.imgs_screenshot() #截图
            raise e
    #查找元素
    def get_element(self,loc):
        self.getlog.get_logging('INFO','{0},查找元素{1}'.format(self.model,loc))
        self.wait_visible(loc)
        try:
            return self.driver.find_element(*loc)
            self.getlog.get_logging('INFO','成功定位到元素')
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:查找{1}元素失败,{2}'.format(self.model,loc,e))
            self.imgs_screenshot(self.model)
            raise e
    '''多元素的时候'''
    def get_elements(self,loc,timeout=30,poll_frequency=0.5):
        self.getlog.get_logging('INFO','{0},查找元素集合{1}'.format(self.model,loc))
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_any_elements_located(loc))
            return self.driver.find_elements(*loc)
            self.getlog.get_logging('INFO','成功定位到元素集合')
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:查找元素集合{1}失败,{2}'.format(self.model,loc,e))
            self.imgs_screenshot()
            raise e
    def get_btn_is_clickable(self,ele):
        return ele.is_enabled()


    def get_text(self,loc):
        self.getlog.get_logging('INFO','获取文本内容')
        print('get_text：',self.model)
        ele = self.get_element(loc)
        try:
            text = ele.text
            return text
            self.getlog.get_logging('INFO','{0}:获取到{1}的text值为{2}'.format(self.model,loc,text))
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:获取元素{1}的text值失败，msg:{2}'.format(self.model,loc,e))
            self.imgs_screenshot()
            raise e


    #输入框操作
    def input_text(self,loc,text):
        self.getlog.get_logging('INFO','{0}:输入文本内容{1}'.format(self.model,text))
        ele = self.get_element(loc)
        try:
            ele.send_keys(text)
            self.getlog.get_logging('INFO','{0}：在元素{1}输入{2}'.format(self.model,loc,text))
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:输入{1}失败，msg:{2}'.format(self.model,loc,e))
            self.imgs_screenshot()
            raise e

    #按键点击操作
    def click_element(self,loc):
        ele = self.get_element(loc)
        try:
            ele.click()
            self.getlog.get_logging('INFO','{0}：点击{1}按键'.format(self.model,loc))
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}按键{1}点击失败,msg:{2}'.format(self.model,loc,e))
            self.imgs_screenshot()
            raise e

    #获取元素的属性
    def get_element_values(self,loc,key):
        self.getlog.get_logging('INFO','获取element属性值')
        ele = self.get_element(loc)
        try:
            value = ele.get_attribute(key)
            self.getlog.get_logging('INFO','{0}成功获取到{1}的{2}属性值为{3}'.format(self.model,loc,key,value))
            return value
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:{1}元素获取"{2}"属性值失败'.format(self.model,loc,key))
            self.imgs_screenshot()
            raise e
    #清除文本信息
    def clear_text(self,loc):
        self.getlog.get_logging('INFO','清除文本信息')
        ele.self.get_element(loc)
        try:
            ele.clear()
            self.getlog.get_logging('INFO','{0}:清除元素{1}的文本内容'.format(self.model,loc))
        except Exception as e:
            self.getlog.get_logging('ERROR','{0}:清除元素{1}的文本内容失败,msg:{2}'.format(self.model,loc,e))
            self.imgs_screenshot()
            raise e


    #封装截图
    def imgs_screenshot(self):
        #model为页面的功能名称
        #filepath = 页面功能名称_当前时间。png
        filepath = os.path.join(dir_config.screenshot_dir,"{0}-{1}.png".format(self.model,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())))
        #截图防范：self.driver.save_screenshot(filepath)
        try:
            self.driver.save_screenshot(filepath)
            self.getlog.get_logging('INFO','截图成功，图片路径为{0}'.format(filepath))
        except Exception as e:
            self.getlog.get_logging('ERROR',"截图失败，{0}".format(e))
            raise e

    #切换窗口
    def switch_new_window(self,name,timeout=30,poll_frequency=0.5):
        '''
        :param name: new代表最新打开一个窗口。default 代表第一个窗口。 其它的值表示为窗口的handles
        '''
        self.getlog.get_logging('INFO','切换窗口操作')
        windows = self.driver.window_handles
        if name =='new':
            try:
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.new_window_is_opened(common_datas.window_handles_list))
                self.driver.switch_to.window(windows[-1])
                common_datas.window_handles_list = windows
                self.getlog.get_logging('INFO','成功切换到最新打开的窗口')
            except Exception as e:
                self.getlog.get_logging('ERROR','切换窗口失败,msg:{}'.format(e))
                self.imgs_screenshot()
                raise e
        else:
            try:
                self.driver.switch_to.window(name)
                self.getlog.get_logging('INFO','成功切换到窗口:{}'.format(name))
            except Exception as e:
                self.getlog.get_logging('ERROR','切换窗口失败,msg:{}'.format(e))
                self.imgs_screenshot()
                raise e

    def switch_iframe(self,loc,timeout =30,poll_frequency=0.5):
        self.getlog.get_logging('INFO','iframe切换操作:')
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(loc))
            self.getlog.get_logging('INFO','切换成功')
        except Exception as e:
            self.getlog.get_logging('ERROR','切换iframe失败')
            self.imgs_screenshot()
            raise e
    
    def switch_alert(self,action):
        self.getlog.get_logging('INFO','切换到alert操作：')
        try:
            alert = self.driver.switch_to.alert
            self.getlog.get_logging('INFO','成功切换到alert')
        except Exception as e:
            self.getlog.get_logging('ERROR','切换到alert失败'.format(e))
        else:
            if action == 'accept':
                alert.accept()
                self.getlog.get_logging('INFO','alert accept')
            else:
                alert.dismiss()
                self.getlog.get_logging('INFO','alert dismiss')




        

    
    
