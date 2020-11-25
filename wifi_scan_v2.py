# -*- coding: utf-8 -*-
import pywifi
import sys
import time
from pywifi import *
import numpy as np


recordTime=10
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]


#print (iface.name())
#if iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
#print ('connected')

#while 1:
for j in range(3):
    runtime=time.time()
    fileName=time.strftime("%Y%m%d%H%M%S", time.localtime())
    #print("started recording "+str(fileName))
    
    #print (iface.name())
    if iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
        print ('now connected then scanning wifi signal.')
        iface.scan()        
        timeDiff=time.time()-runtime
        if (timeDiff<recordTime):
            time.sleep(recordTime-timeDiff)
        result=iface.scan_results()

        print(str(len(result)))
        
        fileprint=open("./wifiscandata/"+str(fileName)+".csv", "a")
        #print (time.ctime())
        fileprint.write("SSID,BSSID,Channel,Signal\n")
        
        result_unique=[]
        for i in range(len(result)):
            if not ((result[i].ssid),str(result[i].bssid),str(result[i].freq),str(result[i].signal)) in result_unique:
                result_unique.append(((result[i].ssid),str(result[i].bssid),str(result[i].freq),str(result[i].signal)))
        #print(result_unique)
        for i in range(len(result_unique)):
            #fileprint.write((result_1[i].ssid)+","+str(result_1[i].bssid)+","+str(result_1[i].freq)+","+str(result_1[i].signal)+"\n")
            fileprint.write((result_unique[i][0])+","+str(result_unique[i][1])+","+str(result_unique[i][2])+","+str(result_unique[i][3])+"\n")
        
    else:
        print ('no interface connected.')
    fileprint.close()
    iface.disconnect()
    result=[]
    