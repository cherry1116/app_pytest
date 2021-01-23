'''
Created on 2020年5月11日

@author: Administrator
'''
from appium.webdriver.common.mobileby import MobileBy

class GongliaoLocator:
    gongliao_btn=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_publish_imchat')
    input_text=(MobileBy().ID,'com.gossip.ziv.gossip:id/et_chat_input')
    gl_back=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_toolbar_back')
    send_btn=(MobileBy().ID,'com.gossip.ziv.gossip:id/btn_submit')
    biaoqing_btn=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_expression')
    
    
    