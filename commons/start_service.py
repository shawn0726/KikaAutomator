import os
import re

from util.log_info import Log_info


def start_devices():
    """
    :return: 返回list（连接的设备device id）
    """
    cmd = os.popen('adb devices')
    device_info = cmd.read()
    cmd.close()
    device_id_list = re.findall(r'(.*?)\t', device_info)
    return device_id_list


def start_appium(port_id, device):
    """
    :param port_id: 启动 appium 服务监听端口号
    :param device: 设备device id
    :return:
    """
    os.system(
        'node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js'
        ' --port %s -U %s --session-override' % (
            str(port_id), device))
    '''
    appium 使用方式
    result = os.system('appium -p %s -bp %s -U %s --session-override' % (
            str(port_id), device))
    '''
    # Log_info().getlog('start-service').debug(result)
    # print("%s,%s,%s" % (str(port_id), device))
