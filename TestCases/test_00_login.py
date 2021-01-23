'''
Created on 2020年5月7日

@author: Administrator
'''
import pytest
import logging
from TestDatas import login_datas as LD
from PageObjects.user_page import UserPage


#登录成功：
#登录： toast

@pytest.mark.usefixtures("loginApp") 
class TestLogin:    
    @pytest.mark.smoke
    def test_login_success(self,loginApp):
        #1首页-注册/登录 点击
        logging.info("************登录用例：正常场景：使用正确的用户名和密码登录**************")
        #2登录页面—输入用户名、密码
        loginApp[1].login(LD.success_data["user"], LD.success_data["passwd"])
        #断言：登录状态
        assert UserPage(loginApp[0]).get_loginStatus()
        