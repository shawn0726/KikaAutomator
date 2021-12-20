import multiprocessing
import os
import time
from multiprocessing.pool import Pool

import xlrd
from appium import webdriver

import pytest
import yaml


device_id_list = []
desired_process = []
screen_size_list = []
driver_pool = []
script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_data_path = script_path_up + '/data/case_data.yml'
test_case_data = yaml.safe_load(open(case_data_path, 'r'))
case_id_data_path = os.path.dirname(os.path.abspath(__file__)) + '/case_id.xlsx'
MAX_POOL_NUMBER = 2


@pytest.fixture(scope='session', autouse=True)
def set_device_id_list():
    device_id_list.clear()
    from commons import start_service
    list1 = start_service.start_devices()
    for i in range(len(list1)):
        device_id_list.append(list1[i])
    return device_id_list
    # return ['2962de230205']


# 解析附加参数
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="0", help="my option: 0 or 1"
    )


@pytest.fixture(scope='session', autouse=True)
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope='session', autouse=True)
def set_driver_pool(cmdopt):
    device_id_list_num = len(device_id_list)
    real_pool_number = min(device_id_list_num, MAX_POOL_NUMBER)
    port_id = 4724
    # bp_id = 99
    sys_port = 8200
    if device_id_list_num != 0:
        p = Pool(real_pool_number)
        print(p)

    port_id = port_id + int(cmdopt)
    # bp_id = bp_id + int(cmdopt)
    sys_port = sys_port + int(cmdopt)
    from util.device_data import keep_port_available
    keep_port_available(port_id)
    try:
        from commons.start_service import start_appium
        p.apply_async(start_appium, args=(port_id, device_id_list[int(cmdopt)],))
    except Exception as e:
        from util.log_info import Log_info
        Log_info().getlog('start-appium-test-case').debug(e)
    # wait(10)
    time.sleep(3)
    from util.device_data import get_platform_version
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
        print('55555555555')
        print(driver)
        print('55555555555')
        driver.implicitly_wait(5)
        from util.log_info import Log_info
        Log_info().getlog('start-driver').debug(driver)
        # 设置默认输入法
        # from page.main_page import MainPage
        print('11111')
        # MainPage(driver).set_default_method().agree_gdpr().back_to_input_page()
        driver_pool.append(driver)
        # return driver_pool
        print('********  ********')
        print(driver_pool)
        print('********  ********')

    except Exception as e:
        Log_info().getlog('start-drive-test-case').debug(e)
    time.sleep(2)

    p.close()
    p.terminate()
    print('77777777777')
    print(driver)
    print('77777777777')
    yield driver


@pytest.fixture
def deliver_event():
    wb = xlrd.open_workbook(filename=case_id_data_path)
    sheet1 = wb.sheet_by_index(0)
    case_id = sheet1.col_values(1)
    pool_id = sheet1.col_values(1)
    case_id.pop(0)
    pool_id.pop(0)

    return case_id, pool_id


@pytest.fixture
def get_device_id_list():
    return device_id_list


@pytest.fixture
def get_driver_pool():
    return driver_pool


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    set_device_id_list()
    set_driver_pool()
