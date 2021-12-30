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

# from lib.start_service import device_id_list, driver_pool

script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_data_path = script_path_up + '/test_auto/data/case_data.yml'
test_case_data = yaml.safe_load(open(case_data_path, 'r'))
case_id_data_path = os.path.dirname(os.path.abspath(__file__)) + '/case_id.xlsx'
# MAX_POOL_NUMBER = 1
device_id_list = []

#调用设备 ID 列表

@pytest.fixture(scope='session', autouse=True)
def set_device_id_list():
    device_id_list.clear()
    list1 = start_devices()
    for i in range(len(list1)):
        device_id_list.append(list1[i])
    return device_id_list
    # return ['2962de230205']



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


@pytest.fixture(scope='session', autouse=True)
def set_driver_pool(cmdopt):
    driver_pool = []
    device_id_list_num = len(device_id_list)
    real_pool_number = 1
    #min(device_id_list_num, MAX_POOL_NUMBER)
    port_id = 4724
    # bp_id = 99
    sys_port = 8200
    if device_id_list_num != 0:
        p = multiprocessing.Pool(real_pool_number)
        print(p)

    port_id = port_id + int(cmdopt)
    # bp_id = bp_id + int(cmdopt)
    sys_port = sys_port + int(cmdopt)
    keep_port_available(port_id)

    try:
        p.apply_async(start_appium, args=(port_id, device_id_list[int(cmdopt)],))
    except Exception as e:
        e
        # Log_info().getlog('start-appium-test-case').debug(e)
    # wait(10)
    time.sleep(3)
    plat_form_version = get_platform_version(device_id_list[int(cmdopt)])

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
                'id': device_id_list[int(cmdopt)]}

        driver = webdriver.Remote('http://localhost:' + str(port_id) + '/wd/hub', caps)
        print(driver,"这是driver")
        # driver = drivers.devices_driver.devs('http://localhost:' + str(port_id) + '/wd/hub', caps)
        driver.implicitly_wait(5)
        driver_pool.append(driver)
        return driver_pool


    except Exception as e:
        e
        pass
    #     # Log_info().getlog('start-drive-test-case').debug(e)
    #     time.sleep(2)
    #     p.close()
    #     p.terminate()
    #     yield driver


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




