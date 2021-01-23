'''
Created on 2020年5月9日

@author: Administrator
'''
from Common.basepage import BasePage
from PageLocators.room_locators import RoomLocator as loc
from PageLocators.index_locators import IndexLocator as loc2


class RoomPage(BasePage):
    #进入房间
    def toRoom(self):
        doc="进入房间"
        
        self.wait_eleVisible(loc.myroom, doc=doc)
        self.click_element(loc.myroom,doc)
    
    def liwu(self):
        doc="礼物"
        return self.is_eleExist(loc.liwu, doc=doc)
    
    def bangdan(self):
        doc="榜单"
        self.wait_eleVisible(loc.bangdan, doc=doc)
        self.click_element(loc.bangdan, doc)
        
    def caifubang(self):
        doc="财富榜"
        return self.is_eleExist(loc.caifubang,doc=doc)
    
    def checkClose(self):
        doc="查找关闭房间按钮"
        return self.is_eleExist(loc.outRoom,  doc=doc)
    
    def outofRoom(self):
        doc1="退出房间按钮"
        doc2="点击退出房间"
        self.wait_eleVisible(loc.outRoom, doc=doc1)
        self.click_element(loc.outRoom, doc=doc1)
        
        self.wait_eleVisible(loc.outRoomend, doc=doc2)
        self.click_element(loc.outRoomend, doc=doc2)
        
        
    def checkOutRoom(self):
        doc="退出房间回到首页"
        return self.is_eleExist(loc2.search_text, doc=doc)
        
        
        
        