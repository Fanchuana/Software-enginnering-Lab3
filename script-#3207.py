import uiautomator2 as u2
import sys
import time

# 第2种连接手机的USB进行连接(安卓模拟器和真机都可以）必须开启USB调试模式
# 手机序列号通过`adb devices`查看
d = u2.connect_usb("892cef58")
print(d.device_info) # 输出详细信息
d.click(0.426, 0.474)
d.click(0.616, 0.372)
d.click(0.078, 0.438)
d.click(0.946, 0.077)
d.click(0.67, 0.294)
d.click(0.724, 0.067)
d.click(0.086, 0.918)
d.click(0.286, 0.744)
d.click(0.491, 0.918)
d.click(0.896, 0.916)

#over
while True:
    d.service("uiautomator").stop()
    time.sleep(2)
    out = d.service("uiautomator").running()
    if not out:
        print("DISCONNECT UIAUTOMATOR2 SUCCESS")
        break
    time.sleep(2)
