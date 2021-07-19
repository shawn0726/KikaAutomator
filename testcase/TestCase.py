import re
import time
from multiprocessing import Pool
import os

import allure
import pytest
from selenium.webdriver.common.by import By

from commons.get_path import get_path_data
from page.input_page import InputPage
from util.device_data import get_vm_size

'''
生成allure报告 2 步：
1、python3 -m pytest testcase/TestCase.py --alluredir report/allure_raw
2、allure generate report/allure_raw -o report/html --clean
'''

screen_size_list = []
test_case_data = get_path_data('/data/case_data.yml')
test_adb_data = get_path_data('/data/adb_data.yml')

# 设置页面右上角back键
_xpath_locator_setting_back = (By.XPATH,
                               '//android.widget.ImageButton[@content-desc="转到上一层级"]')
# GDPR 弹窗相关控件
_gdpr_pop_up = (
    By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
_gdpr_disagree = (By.ID,
                  'com.huawei.ohos.inputmethod:id/btn_deny')
_gdpr_agree = (By.ID,
               'com.huawei.ohos.inputmethod:id/btn_ok')
_gdpr_learn_more = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_content2')
_input_text_view = (By.CLASS_NAME, 'android.widget.EditText')
_message_input_box = (By.ID, 'com.google.android.apps.messaging:id/compose_message_text')
_address_book_dialog = (By.ID, 'com.android.packageinstaller:id/dialog_container')


@allure.story('英文键盘，输字母后删除')
@pytest.mark.parametrize('case_number', '0')
# 通过 case_number 在 case_id 表中查询，对应的 case 使用哪个 driver
def test_InputMethod_SCB_func_01_01_01_0001(get_device_id_list, get_driver_pool, deliver_event,
                                            case_number):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(deliver_event[int(case_number)])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    if input_page.find_element_by_id('com.android.packageinstaller:id/dialog_container'):
        input_page.find_element_by_id_click('com.android.packageinstaller:id/permission_allow_button')
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.input_characters(test_case_data['func_01_01_01_0001']['word1'], device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.input_characters(',', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters(test_case_data['func_01_01_01_0001']['word2'], device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == 'hello ,worl'
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('检查首字母大写功能')
@pytest.mark.parametrize('case_number', '1')
def test_InputMethod_SCB_func_01_01_01_0003(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[int(case_number)])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(
        'adb -s %s shell am start -a android.intent.action.SENDTO -d sms:10086' % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.google.android.apps.messaging:id/compose_message_text')
    # 有的手机首次调起键盘后，可能会弹起'获取联系人权限'的系统弹框
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    time.sleep(2)
    input_page.find_element_by_id_click(
        'com.android.mms:id/embedded_text_editor')  # com.google.android.apps.messaging:id/compose_message_text
    if input_page.find_element_by_id('com.android.packageinstaller:id/dialog_container'):
        input_page.find_element_by_id_click('com.android.packageinstaller:id/permission_allow_button')
        input_page.find_element_by_id_click('com.google.android.apps.messaging:id/compose_message_text')
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.input_characters(test_case_data['func_01_01_01_0003']['word'], device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_id('com.android.mms:id/embedded_text_editor').text
    assert text == 'Qwerty '
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('检查长按方法')
@pytest.mark.parametrize('case_number', '3')
def test_InputMethod_SCB_func_01_01_01_0003(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[int(case_number)])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('配置页面')
@pytest.mark.parametrize('case_number', '4')
def test_InputMethod_SCB_func_01_01_01_0004(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[int(case_number)])
    os.system('adb -s %s shell am start -S com.xinmei365.emptyinput/.MainActivity' % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system('adb -s %s shell input tap 500 500' % device_id_list[which_driver_pool])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    time.sleep(2)
    input_page.to_which_submenu('Sound', screen_size_list[0], screen_size_list[1])
    time.sleep(2)
    input_page.adjust_vibration('max', screen_size_list[0], screen_size_list[1])


@pytest.mark.parametrize('case_number', '4')
def test_func(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[int(case_number)])
    os.system('adb -s %s shell am start -S com.xinmei365.emptyinput/.MainActivity' % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system('adb -s %s shell input tap 500 500' % device_id_list[which_driver_pool])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    input_page.tap_menu(screen_size_list[0], screen_size_list[1])
    time.sleep(2)
    keyboard_setting_page = input_page.to_which_submenu('Settings', screen_size_list[0], screen_size_list[1])
    time.sleep(2)
    keyboard_setting_page.to_language_setting_page()
    # from page.keyboard_setting_page import KeyboardSettingPage
    # keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    # keyboard_setting_page.find_element_by_text_click('语言')


    # input_page.clipboard_func('One', 'Paste', screen_size_list[0], screen_size_list[1])


if __name__ == '__main__':
    pytest.main()
