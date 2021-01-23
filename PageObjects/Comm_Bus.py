'''
Created on 2020年5月7日

@author: Administrator
'''

from Common.basepage import BasePage
import time

class CommBus(BasePage):
    #处理欢迎页面    
    def do_welcome(self):
        time.sleep(7)
        #如果没有找到首页的元素、或者不包含MainActivity,那么就是在欢迎页面
        curAct=self.driver.current_activity
        if curAct.find("MainActivity")==-1:
            #滑动欢迎页面至首页
            #左滑三次，点击立即体验
            size=BasePage(self.driver).get_size()
            for i in range(3):
                BasePage(self.driver).swipe_left(size)
                time.sleep(1)
            #点击立即体验
                 
    #导航栏
    
    #是否设置手势密码
    def is_setGesture(self,action=False):
        #有没有设置手势密码的弹框-5秒
        #如果没有，是设置还是不设置呢？
        if action==False:
            pass #点击不设置
        else:
            pass #点击立即设置
        