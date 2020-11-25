import pywifi
import sys
import time
from pywifi import *
recordTime=5


wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
#print (iface.name())
#if iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
#print ('connected')
while 1:
    now=time.time()
    fileName=time.time()
    print("started recording "+str(fileName))
    fp=open("./wifiscandata/"+str(fileName)+".txt", "a")
    iface.scan()
    result=iface.scan_results()
    print (time.ctime())
    fp.write(time.ctime()+"\n")
    for i in range(len(result)):
        print (result[i].ssid, result[i].signal)
        fp.write(result[i].ssid+","+str(result[i].signal)+"\n")
    timeDiff=time.time()-now
    if (timeDiff<recordTime):time.sleep(recordTime-timeDiff)
    fp.close()
