'''
Created on 2020年5月8日

@author: Administrator
'''

from appium.webdriver.common.mobileby import MobileBy

class IndexLocator:
#     login_btn=(MobileBy().ID,'com.gossip.ziv.gossip:id/ed_id')
    search_text=(MobileBy().ID,'com.gossip.ziv.gossip:id/tv_search')
#     navlist=(MobileBy().CLASS_NAME,'android.widget.FrameLayout')
#     nav_ph=navlist[1]
    
    bang=(MobileBy().CLASS_NAME,'android.widget.TextView')
    userid=(MobileBy().ID,'com.gossip.ziv.gossip:id/tv_mine_id')
    
    