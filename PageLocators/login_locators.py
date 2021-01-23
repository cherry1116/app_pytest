'''
Created on 2020年5月7日

@author: Administrator
'''

from appium.webdriver.common.mobileby import MobileBy

class LoginLocator:
    
    user_input=(MobileBy().ID,'com.gossip.ziv.gossip:id/ed_id')
    passwd_input=(MobileBy().ID,'com.gossip.ziv.gossip:id/ed_pwd')
    login_button=(MobileBy().ID,'com.gossip.ziv.gossip:id/btn_login')