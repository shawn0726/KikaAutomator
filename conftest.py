# coding: utf-8


'''
全局配置
'''
import logging
import multiprocessing
import os
import time

import xlrd
import pytest
import yaml
from appium import webdriver

# from drivers.android import device_android
from lib.device_data import keep_port_available, start_appium, get_platform_version, start_devices


script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_data_path = script_path_up + '/KikaAutomator/data/case_data.yml'
test_case_data = yaml.safe_load(open(case_data_path, 'r'))
case_id_data_path = os.path.dirname(os.path.abspath(__file__)) + '/case_id.xlsx'
MAX_POOL_NUMBER = 2
device_id_list = []

#调用设备 ID 列表
@pytest.fixture(scope='session', autouse=True)
def set_device_id_list():
    device_id_list.clear()
    list1 = start_devices()
    for i in range(len(list1)):
        device_id_list.append(list1[i])
    return device_id_list




# 解析附加参数
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="0", help="my option: 0 or 1"
    )

# 选择指令
@pytest.fixture(scope='session', autouse=True)
def cmdopt(request):
    return request.config.getoption("--cmdopt")





# 分发devicesID
@pytest.fixture
def deliver_event():
    wb = xlrd.open_workbook(filename=case_id_data_path)
    sheet1 = wb.sheet_by_index(0)
    case_id = sheet1.col_values(1)
    pool_id = sheet1.col_values(1)
    case_id.pop(0)
    pool_id.pop(0)
    return case_id, pool_id

#获取驱动程序池
# @pytest.fixture
# def get_driver_pool():
#     driver_pool = []
#     return driver_pool

# 设置驱动池
@pytest.fixture(scope='session', autouse=True)
def set_driver_pool():
    driver_pool = []
    device_id_list_num = len(device_id_list)
    real_pool_number = min(device_id_list_num, MAX_POOL_NUMBER) #人为控制设备运行数量
    port_id = 4724
    # bp_id = 99
    sys_port = 8200
    if device_id_list_num != 0:
        p = multiprocessing.Pool(real_pool_number)
        print(p)

        for i in range(real_pool_number):
            port_id = port_id + int(i)
            # bp_id = bp_id + int(cmdopt)
            sys_port = sys_port + int(i)
            keep_port_available(port_id)
            try:
                p.apply_async(start_appium, args=(port_id, device_id_list[int(i)],))
            except Exception as e:
                print('报错喽---%s'%e)
            time.sleep(3)
            plat_form_version = get_platform_version(device_id_list[int(i)])

            '''
            com.huawei.ohos.inputmethod
            '''
            try:
                caps = {'platformName': 'Android', 'platformVersion': plat_form_version, 'deviceName': 'nexus 6p',
                        'newCommandTimeout': 0,
                        'appPackage': 'com.xinmei365.emptyinput',
                        'appActivity': 'com.xinmei365.emptyinput.MainActivity',
                        'systemPort': sys_port,
                        'automationName': 'UiAutomator2',
                        'disableSuppressAccessibilityService': True,
                        'enableMultiWindows': True,
                        'allowInvisibleElements': True,
                        'ignoreUnimportantViews': False,
                        'id': device_id_list[int(i)]}

                driver = webdriver.Remote('http://localhost:' + str(port_id) + '/wd/hub', caps)
                # driver = drivers.devices_driver.devs('http://localhost:' + str(port_id) + '/wd/hub', caps)
                driver.implicitly_wait(5)
                driver_pool.append(driver)
                # return driver_pool
            except Exception as e:
                print('启动失败---%s'%e)
                # Log_info().getlog('start-drive-test-case').debug(e)
        time.sleep(2)
        p.close()
        p.terminate()
        yield driver_pool


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    set_driver_pool()




# #初始化设备
#
# @pytest.fixture(scope='session',autouse=True)
# def driver():
#     try:
#         driver = drivers.android.device_android()
#         # driver = drivers.android.device_android("192.168.129.93")
#         # log.info("已连接设备:{}".format(driver.info['productName']))
#         return driver
#     except Exception as e:
#         log.info("初始化driver异常!{}".format(e))

# def pytest_collection_modifyitems(items):
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")




