'''
Created on 2020年5月11日

@author: Administrator
'''
from Common.basepage import BasePage
from PageLocators.paihang_locators import PaihangLocator as loc

class PaiPage(BasePage):
    def checkPaihang(self):
        doc="查看是否打开排行页面"
        return self.is_eleExist(loc.no1,  doc=doc)