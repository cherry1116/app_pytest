'''
Created on 2020年5月11日

@author: Administrator
'''
import pytest
import logging
from PageObjects.pai_page import PaiPage

@pytest.mark.usefixtures("goPaihang") 
class TestPaihang:  
    @pytest.mark.smoke
    def test_paihang_success(self,goPaihang):
        logging.info("*********点击导航栏排行榜**********************")
        goPaihang[0].tap([(405,1836)],1000)
        assert PaiPage(goPaihang[0]).checkPaihang()
        
