import os
import platform
import re
from util.log_info import Log_info


# 获取屏幕分辨率
def get_vm_size(device_id_list, screen_size_list):
    cmd = os.popen('adb -s %s shell wm size' % device_id_list)
    vm_size = cmd.read()
    cmd.close()
    print(vm_size, type(vm_size))
    vm_size_list = re.findall(r'(\d+)', vm_size)
    width = vm_size_list[0]
    screen_size_list.append(width)
    height = vm_size_list[1]
    screen_size_list.append(height)
    return screen_size_list


# 查询端口号是否可用
def keep_port_available(port_id):
    which_system = platform.system().lower()
    print('which_system: %s' % which_system)
    if 'darwin'in which_system:
        cmd = os.popen('lsof -i tcp:%d' % port_id)
        port_available = cmd.read()
        cmd.close()
        pid = re.findall(r'(\s\d+\s)', port_available)
        port_available_last = ''.join(pid).strip()
        try:
            os.system('kill %s' % port_available_last)
        except Exception as e:
            Log_info().getlog('kill-port').debug(e)
    else:
        cmd = os.popen('netstat -aon | findstr "%d" ' % port_id)
        port_available = cmd.read()
        cmd.close()
        pid = re.findall(r'(\s\d+\s)', port_available)
        port_available_last = ''.join(pid).strip()
        try:
            os.system('taskkill /F /PID %s' % port_available_last)
        except Exception as e:
            Log_info().getlog('kill-port').debug(e)


# 查询系统版本号
def get_platform_version(device_id):
    cmd = os.popen('adb -s %s shell getprop ro.build.version.release' % device_id)
    platform_version = cmd.read()
    cmd.close()
    return platform_version.replace('\n', '')
