import uiautomator2 as u2
import sys
import time
d = u2.connect_usb("892cef58")
print(d.device_info) # 输出详细信息
d.click(0.408, 0.474)
d.click(0.293, 0.691)
d.click(0.247, 0.519)
d.click(0.817, 0.665)
d.press("back")
d.press("back")
d.press("back")
#over
while True:
    d.service("uiautomator").stop()
    time.sleep(2)
    out = d.service("uiautomator").running()
    if not out:
        print("DISCONNECT UIAUTOMATOR2 SUCCESS")
        break
    time.sleep(2)