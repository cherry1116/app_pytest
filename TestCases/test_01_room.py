'''
Created on 2020年5月9日

@author: Administrator
'''
import pytest
import logging 
from PageObjects.room_page import RoomPage

@pytest.mark.usefixtures("gotoRoom") 
class TestRoom:
    @pytest.mark.smoke
    def test_toRoom_success(self,gotoRoom):
        logging.info("************进入房间用例：正常场景：点击房间进入房间*************")
        gotoRoom[1].toRoom()
        assert RoomPage(gotoRoom[0]).liwu()
        
    @pytest.mark.smoke
    def test_OutRoom_success(self,gotoRoom):
        logging.info("*************退出房间*****************************")
        gotoRoom[1].outofRoom()
        assert RoomPage(gotoRoom[0]).checkOutRoom()
        
             
        
    