'''
Created on 2020年5月7日

@author: Administrator
'''
from Common.basepage import BasePage
from PageLocators.login_locators import LoginLocator as loc
class LoginPage(BasePage):
    #登录操作
    def login(self,username,passwd):
        #输入用户名
        #输入密码
        doc="登录页面_登录功能"
        self.wait_eleVisible(loc.user_input, doc=doc)
        self.input_text(loc.user_input,username,doc)
        self.input_text(loc.passwd_input,passwd,doc)
        self.click_element(loc.login_button,doc)
        
        
    def get_wrongMsg_from_loginPage(self):
        pass
    
    
        