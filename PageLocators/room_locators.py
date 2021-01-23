'''
Created on 2020年5月9日

@author: Administrator
'''
from appium.webdriver.common.mobileby import MobileBy
class RoomLocator:
#     roomid=(MobileBy().ID,'com.gossip.ziv.gossip:id/roomview_1')
    myroom=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_my_room')
    liwu=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_gift')
    bangdan=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_room_ranking')
    caifubang=(MobileBy().CLASS_NAME,'android.widget.FrameLayout')
    outRoom=(MobileBy().ID,'com.gossip.ziv.gossip:id/iv_room_menu')
    outRoomend=(MobileBy().ID,'com.gossip.ziv.gossip:id/tv_exit')
    