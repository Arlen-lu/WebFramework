import sys
import os
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from PageLocators.ele_locator import AccountLocators as loc
from Common.BasePages import BasePage

class AccountPage(BasePage):

    def __init__(self,driver,getlog,model=None):
        super(AccountPage,self).__init__(getlog,model)
        self.driver = driver
        self.getlog =getlog
        self.model = model
    
    def get_available_balance(self):
        balance = self.get_text(loc.available_balance).replace('元','')
        return balance