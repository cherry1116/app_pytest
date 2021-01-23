'''
Created on 2020年5月11日

@author: Administrator
'''
from Common.basepage import BasePage
from PageLocators.gongliao_locators import GongliaoLocator as loc
from PageLocators.index_locators import IndexLocator as loc2

class GongliaoPage(BasePage):
    def clickGongliao(self):
        doc="点击公聊广场"
        size=BasePage(self.driver).get_size()
        BasePage(self.driver).swipe_gongliao(size)
        self.wait_eleVisible(loc.gongliao_btn, doc=doc)
        self.click_element(loc.gongliao_btn, doc=doc)
        
        
    def getInput(self):
        doc="消息输入框"
        return self.is_eleExist(loc.input_text, doc=doc)
    
    def inputLiaotian(self):
        doc="输入聊天内容"
        self.wait_eleVisible(loc.biaoqing_btn, doc=doc)
        self.click_element(loc.biaoqing_btn, doc=doc)
    
    def sendInput(self):
        doc="输入聊天内容,点击发送聊天内容"
        return self.is_eleExist(loc.gl_back, doc=doc)
          
    def clickBack(self):
        doc="点击返回首页"
        self.click_element(loc.gl_back, doc=doc)
        
    def checkBack(self):
        doc="检查是否返回首页"
        return self.is_eleExist(loc2.search_text,  doc=doc)
        