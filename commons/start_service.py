import os
import re

from util.log_info import Log_info


def start_devices():
    device_info = os.popen('adb devices').read()
    device_id_list = re.findall(r'(.*?)\t', device_info)
    return device_id_list


def start_appium(port_id, bp_id, device):
    result = os.system(
        'node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js'
        ' --port %s --bootstrap-port %s -U %s --session-override' % (
            str(port_id), str(bp_id), device))
    Log_info().getlog('start-service').debug(result)
    print("%s,%s,%s" % (str(port_id), str(bp_id), device))
