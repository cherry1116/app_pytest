'''
Created on 2020年5月7日

@author: Administrator
'''
import pytest
from Common.dir_config import caps_dir
import yaml
from appium import webdriver
from PageObjects.Comm_Bus import CommBus
from PageObjects.login_page import LoginPage
from PageObjects.room_page import RoomPage
from PageObjects.Gongliao_Page import GongliaoPage
from PageObjects.pai_page import PaiPage


#登录用例使用的前置后置
@pytest.fixture
def startApp():
    #准备服务器参数，与appium server进行连接。noReset=True
    driver=baseDriver()
    #1 要不要判断欢迎页面是否存在？
    CommBus(driver).do_welcome(driver)
    #2 要不要判断当前用户是否已登录？——接口
    # 如果已登录，那么先退出 ——接口

#除登录以外通用的前置条件
@pytest.fixture
def loginApp():
    global driver
    print("===========所有测试用例之前的，setup===整个测试类只执行一次==========")
    #准备服务器参数，与appium server进行连接 noReset=True
    driver=baseDriver()
    #1 要不要判断欢迎页面是否存在？
#     CommBus(driver).do_welcome(driver)
    #2 判断是否是已登录状态 若没有登录则进行登录操作
    lg=LoginPage(driver)
    yield (driver,lg)
    print("=========所有测试用例之后的，teardown===整个测试类只执行一次=========")
#     driver.quit()
    
    #3 是否有设置手势密码的框 不设置
    
@pytest.fixture
def gotoRoom():
    global driver 
    rg=RoomPage(driver)
    yield(driver,rg)
    

@pytest.fixture 
def gotoGongliao():
    global driver 
    gg=GongliaoPage(driver)
    yield(driver,gg)   

@pytest.fixture 
def goPaihang():
    global driver
    pg=PaiPage(driver)
    yield(driver,pg)

    

def baseDriver(server_port=4444,noReset=None,automationName=None,**kwargs):
    #将默认的配置数据读取出来
    fs=open(caps_dir+"\caps.yaml",'r')
    desired_caps=yaml.load(fs)
    #调整参数
    if noReset is not None:
        desired_caps["noReset"]=noReset
    if automationName is not None:
        desired_caps["automationName"]=automationName
    #kwargs
    #返回一个启动对象 -driver
    return webdriver.Remote('http://127.0.0.1:{0}/wd/hub'.format(server_port),desired_caps)


