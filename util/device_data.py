import os
import re
from util.log_info import Log_info


def get_vm_size(device_id_list, screen_size_list):
    vm_size = os.popen('adb -s %s shell wm size' % device_id_list).read()
    print(vm_size, type(vm_size))
    vm_size_list = re.findall(r'([0-9]\d*\d*[0-9])', vm_size)
    width = vm_size_list[0]
    screen_size_list.append(width)
    height = vm_size_list[1]
    screen_size_list.append(height)
    return screen_size_list


def keep_port_available(port_id):
    port_available = os.popen('lsof -i tcp:%d' % port_id).read()
    pid = re.findall(r'(\s\d+\s)', port_available)
    port_available_last = ''.join(pid).strip()
    try:
        os.system('kill %s' % port_available_last)
    except Exception as e:
        Log_info().getlog('kill-port').debug(e)


def get_platform_version(device_id):
    platform_version = os.popen('adb -s %s shell getprop ro.build.version.release' % device_id).read()
    return platform_version.replace('\n', '')
