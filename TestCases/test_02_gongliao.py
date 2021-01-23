'''
Created on 2020年5月11日

@author: Administrator
'''
import pytest
import logging
from PageObjects.Gongliao_Page import GongliaoPage
import time

@pytest.mark.usefixtures("gotoGongliao") 
class TestGongliao:  
    @pytest.mark.smoke
    def test_gongliao_success(self,gotoGongliao):
        logging.info("************进入公聊广场：正常场景：点击进入公聊广场*************")
        gotoGongliao[1].clickGongliao()
        assert GongliaoPage(gotoGongliao[0]).getInput()
        
    @pytest.mark.smoke
    def test_liao_success(self,gotoGongliao):
        logging.info("***********输入发送聊天***********************")
        time.sleep(1)
        gotoGongliao[1].inputLiaotian()
        time.sleep(1)
        gotoGongliao[0].tap([(140.5,1467)],1000)
        assert GongliaoPage(gotoGongliao[0]).sendInput()
       
    @pytest.mark.smoke
    def test_gongliaoback_success(self,gotoGongliao):
        logging.info("***********返回首页***************")
        gotoGongliao[1].clickBack()
        assert GongliaoPage(gotoGongliao[0]).checkBack()
        