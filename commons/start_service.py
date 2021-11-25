import os
import re

from util.log_info import Log_info


def start_devices():
    cmd = os.popen('adb devices')
    device_info = cmd.read()
    cmd.close()
    device_id_list = re.findall(r'(.*?)\t', device_info)
    return device_id_list


def start_appium(port_id, bp_id, device):
    result = os.system(
        'node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js'
        ' --port %s --bootstrap-port %s -U %s --session-override' % (
            str(port_id), str(bp_id), device))
    '''
    appium 使用方式
    result = os.system('appium -p %s -bp %s -U %s --session-override' % (
            str(port_id), str(bp_id), device))
    '''
    Log_info().getlog('start-service').debug(result)
    print("%s,%s,%s" % (str(port_id), str(bp_id), device))
