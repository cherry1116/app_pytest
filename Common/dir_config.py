'''
Created on 2020年5月7日

@author: Administrator
'''
import os 
base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
testdatas_dir=os.path.join(base_dir,"TestDatas")
testcases_dir=os.path.join(base_dir,"TestCases")
htmlreport_dir=os.path.join(base_dir,"Outputs/Reports")
logs_dir=os.path.join(base_dir,"Outputs/Logs")
screenshot_dir=os.path.join(base_dir,"Outputs/Screenshots")
caps_dir=os.path.join(base_dir,"Desired_Caps")