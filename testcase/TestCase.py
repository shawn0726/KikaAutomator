import re
import time
from multiprocessing import Pool
import os

import allure
import pytest
from selenium.webdriver.common.by import By

import golVar
from commons.base_function import PATH
from commons.get_path import get_path_data
from page.input_page import InputPage

from util.device_data import get_vm_size

'''
生成allure报告 2 步：
1、python3 -m pytest testcase/TestCase.py --alluredir report/allure_raw --clean-alluredir
2、allure generate report/allure_raw -o report/html --clean
'''

screen_size_list = []
test_case_data = get_path_data('/data/case_data.yml')
test_adb_data = get_path_data('/data/adb_data.yml')

# GDPR 弹窗相关控件
_gdpr_pop_up = (
    By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
_gdpr_disagree = (By.ID,
                  'com.kika.photon.inputmethod:id/btn_deny')
_gdpr_agree = (By.ID,
               'com.kika.photon.inputmethod:id/btn_ok')
_gdpr_learn_more = (By.ID, 'com.kika.photon.inputmethod:id/tv_content2')
_input_text_view = (By.CLASS_NAME, 'android.widget.EditText')
_message_input_box = (By.ID, 'com.google.android.apps.messaging:id/compose_message_text')
_address_book_dialog = (By.ID, 'com.android.packageinstaller:id/dialog_container')


@allure.story('检查删除键功能')
# 通过 case_number 在 case_id 表中查询，对应的 case 使用哪个 driver
def test_InputMethod_SCB_Func_01_01_01_0001(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    driver = set_driver_pool
    input_page = InputPage(driver)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
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


@allure.story('检查长按删除键功能')
# 通过 case_number 在 case_id 表中查询，对应的 case 使用哪个 driver
def test_InputMethod_SCB_Func_01_01_01_0002(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.input_characters('hello', device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.input_characters(',', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters('world', device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.long_press('delete', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.long_press('delete', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == ''
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('检查首字母大写功能')
def test_InputMethod_SCB_Func_01_01_01_0003(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(
        test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.google.android.apps.messaging:id/compose_message_text')
    # 有的手机首次调起键盘后，可能会弹起'获取联系人权限'的系统弹框
    # os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
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
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
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


@allure.story('检查大小写切换键功能-大写锁定')
def test_InputMethod_SCB_Func_01_01_01_0008(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    pic_before = input_page.screenshot2('pic1')
    input_page.input_characters('shift', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters('shift', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    pic_after = input_page.screenshot2('pic2')
    input_page.input_characters('hello', device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.input_characters(',', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters('world', device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    result = input_page.compare(pic_before, pic_after)
    print(result)
    print(text)
    assert text == 'HELLO ,WORLD '


@allure.story('检查按键点击与上屏功能')
def test_InputMethod_SCB_Func_01_01_01_0009(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.input_characters('abcdef', device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == 'abcdef '


@allure.story('检查长按弹泡功能')
def test_InputMethod_SCB_Func_01_01_01_00010(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_setting()
    time.sleep(1)
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).to_page_setting_page().check_bubble_capitalization('noselect')
    from page.page_setting_page import PageSettingPage
    PageSettingPage(set_driver_pool).back_to_setting_page().back_to_input_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    '''
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.uncheck_language_list('中文')
    language_setting_page.back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    '''
    input_page.long_press('qwertyuiopasdfghjklzxcvbnm', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == '1234567890@#$%&-+()*\"\':;!?'


@allure.story('检查空格键功能使用')
def test_InputMethod_SCB_Func_01_01_01_00011(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.input_characters('hello', device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == 'hello '


@allure.story('检查空格键功能使用')
def test_InputMethod_SCB_Func_01_01_01_00013(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.long_press('space', device_id_list[which_driver_pool],
                          screen_size_list[0], screen_size_list[1])
    input_page.deal_sys_dialog('//*[@resource-id="com.android.packageinstaller:id/permission_message"', '允许')
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('space', device_id_list[which_driver_pool],
                          screen_size_list[0], screen_size_list[1])
    assert input_page.is_element_exist('语言选择按键，双击选择键盘语言') is True
    input_page.menu_back()


@allure.story('检查句号长按弹泡功能')
def test_InputMethod_SCB_Func_01_01_01_00016(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
    英文键盘长按，无其他可选符号，是否是版本差异
    '''
    pass


@allure.story('中文键盘检查语言切换键')
def test_InputMethod_SCB_Func_01_01_01_00036(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    # 26键点击中/英切换键
    # 英文键盘
    pic_26_english = input_page.screenshot2('26键英文')
    pic_26_english_path = PATH(os.getcwd() + "/testcase/TestResult/26键英文.png")
    result_26_english = input_page.compare(pic_26_english_path, pic_26_english)
    pytest.assume(result_26_english == 0.0)
    input_page.input_characters('q', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    pytest.assume(text == 'q ')
    # 点击中/英切换键，检查是否为中文键盘
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    pic_26_chinese = input_page.screenshot2('26键中文')
    pic_26_chinese_path = PATH(os.getcwd() + "/testcase/TestResult/26键中文.png")
    result_26_chinese = input_page.compare(pic_26_chinese_path, pic_26_chinese)
    pytest.assume(result_26_chinese == 0.0)
    input_page.input_characters('q', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    pytest.assume(text == '去')
    # 进入键盘布局，切换为 9 键
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('9键')
    pic_9 = input_page.screenshot2('9键中文')
    pic_9_path = PATH(os.getcwd() + "/testcase/TestResult/9键中文.png")
    result_9 = input_page.compare(pic_9_path, pic_9)
    pytest.assume(result_9 == 0.0)
    input_page.input_characters('a', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    pytest.assume(text == '啊')
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    # 使用英文布局
    golVar.set_value('language_layout', 'relative_layout_en')
    # 切换为英文键盘，清空输入框
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.input_characters('q', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    pytest.assume(text == 'q ')
    # 进入键盘布局，切换为笔画
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('笔画')
    pic_bihua = input_page.screenshot2('笔画中文')
    pic_bihua_path = PATH(os.getcwd() + "/testcase/TestResult/笔画中文.png")
    result_bihua = input_page.compare(pic_bihua_path, pic_bihua)
    pytest.assume(result_bihua == 0.0)
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    golVar.set_value('language_layout', 'relative_layout_en')
    # 切换为英文键盘，清空输入框
    input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    # 进入键盘布局，切换为手写
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('手写键盘')
    pic_shouxie = input_page.screenshot2('手写中文')
    pic_shouxie_path = PATH(os.getcwd() + "/testcase/TestResult/手写中文.png")
    result_shouxie = input_page.compare(pic_shouxie_path, pic_shouxie)
    pytest.assume(result_shouxie == 0.0)
    # 切换为英文键盘，清空输入框
    # 进入语言添加页面，添加语言
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    golVar.set_value('language_layout', 'relative_layout_en')
    input_page.language_picker_list('更多语言...')
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.add_language_list2('中文', 'zh_HK')
    language_setting_page.add_language_list2('中文', 'zh_TW')
    language_setting_page.back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    golVar.set_value('language_layout', '注音')
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    # 添加注音键盘
    input_page.language_picker_list('中文（注音）')
    pic_zhuyin = input_page.screenshot2('注音中文')
    pic_zhuyin_path = PATH(os.getcwd() + "/testcase/TestResult/注音中文.png")
    result_zhuyin = input_page.compare(pic_zhuyin_path, pic_zhuyin)
    pytest.assume(result_zhuyin == 0.0)
    # 添加仓颉键盘
    # golVar.set_value('language_layout', '仓颉')
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('中文（倉頡）')
    pic_cangjie = input_page.screenshot2('倉頡中文')
    pic_cangjie_path = PATH(os.getcwd() + "/testcase/TestResult/倉頡中文.png")
    result_cangjie = input_page.compare(pic_cangjie_path, pic_cangjie)
    pytest.assume(result_cangjie == 0.0)


@allure.story('单手键盘初始状态和基础功能检查')
def test_InputMethod_SCB_Func_01_02_0003(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 清除输入法数据
    os.system('adb -s %s shell pm clear com.kika.photon.inputmethod' % device_id_list[which_driver_pool])
    input_page.set_default_inputmethod('ziyan')
    time.sleep(3)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(1)
    input_page.deal_gdpr_informal()
    time.sleep(2)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('单手模式')
    input_page.switch_keyboard_to_opposite()
    input_page.return_to_normal()


@allure.story('检查悬浮键盘模式各功能使用')
def test_InputMethod_SCB_Func_01_03_0010(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    # 进入悬浮键盘模式
    input_page.to_which_keyboard_mode('悬浮键盘')
    time.sleep(2)
    # 依次按上、左、右、下 4 个方向移动悬浮键盘
    input_page.float_to_move('up', 100)
    input_page.float_to_move('left', 100)
    input_page.float_to_move('right', 100)
    input_page.float_to_move('down', 100)
    # 隐藏键盘后再调起键盘
    input_page.menu_back()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    # 点击 menu
    input_page.tap_menu()
    # 切换键盘布局：手写键盘、9键、笔画、26键
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('手写键盘')
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('9键')
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('笔画')
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('26键')
    # 点击进入主题，改变主题，换第一套然后回到输入页面
    input_page.tap_menu()
    input_page.change_theme().switch_them1()
    from page.theme_setting_page import ThemeSettingPage
    ThemeSettingPage(set_driver_pool).back_to_previous_page()
    ThemeSettingPage(set_driver_pool).back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    # 编辑键盘，改动大小

    input_page.tap_menu()
    input_page.tap_adjust_size()
    input_page.adjust_size('a', 'up', 100, screen_size_list[0], screen_size_list[1])
    input_page.adjust_size('b', 'down', 100, screen_size_list[0], screen_size_list[1])
    input_page.adjust_size('c', 'left', 100, screen_size_list[0], screen_size_list[1])
    input_page.adjust_size('d', 'right', 100, screen_size_list[0], screen_size_list[1])
    input_page.float_finish_resize()
    # 编辑键盘恢复默认大小
    input_page.tap_menu()
    input_page.tap_adjust_size()
    input_page.float_restore_default()
    # 点击剪切板，粘贴第一条内容
    input_page.tap_menu()
    input_page.tap_clipboard()
    input_page.clipboard_func(1, '粘贴')
    input_page.menu_back()
    # 点击编辑按钮，并进行相关操作
    input_page.tap_menu()
    input_page.tap_edit()
    input_page.edit_operation('全选')
    input_page.edit_operation('剪切')
    input_page.edit_operation('粘贴')
    input_page.edit_operation('句首')
    input_page.edit_operation('句尾')
    input_page.edit_operation('句首')
    input_page.edit_operation('选择')
    input_page.edit_operation('right')
    input_page.edit_operation('复制')
    input_page.edit_operation('粘贴')
    input_page.edit_operation('删除')
    input_page.edit_operation('回车')
    input_page.edit_operation('剪切板')
    input_page.clipboard_func(1, '粘贴')
    input_page.menu_back()
    # 声音振动调节
    input_page.tap_menu()
    input_page.tap_sound_vibration()
    input_page.adjust_vibration(1)
    input_page.adjust_vibration(0.5)
    input_page.adjust_vibration(0.01)
    input_page.adjust_sound(1)
    input_page.adjust_sound(0.5)
    input_page.adjust_sound(0.01)
    input_page.enter_keyboard_sound_page()
    from page.sound_effect_page import SoundEffectPage
    SoundEffectPage(set_driver_pool).switch_sound9().back_to_previous_page()
    SoundEffectPage(set_driver_pool).back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.tap_menu()
    input_page.tap_setting()
    time.sleep(2)
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).back_to_previous_page()

    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.float_to_normal()


@allure.story('检查键盘初始状态和基础功能')
def test_InputMethod_SCB_Func_01_04_0002(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 清除输入法数据
    os.system('adb -s %s shell pm clear com.kika.photon.inputmethod' % device_id_list[which_driver_pool])
    input_page.set_default_inputmethod('ziyan')
    time.sleep(5)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.deal_gdpr_informal()
    time.sleep(5)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('拇指模式')
    pic_muzhi = PATH(os.getcwd() + "/testcase/TestResult/拇指键盘.png")
    pic = input_page.screenshot2('拇指键盘')
    result = input_page.compare(pic_muzhi, pic)
    assert result == 0.0
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('普通键盘')


@allure.story('使用外接键盘输入字符能够正常展示')
def test_InputMethod_SCB_Func_01_05_0005(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
        外界键盘？？？
    '''


@allure.story('显示一元联想词语言确认')
def test_InputMethod_SCB_Func_01_05_0034(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
            外接键盘？？？
    '''


@allure.story('简体中文支持手写键盘')
def test_InputMethod_SCB_Func_01_07_0001(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    else:
        print('当前为中文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    time.sleep(3)
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('手写键盘')
    pic_muzhi = PATH(os.getcwd() + "/testcase/TestResult/手写中文.png")
    pic = input_page.screenshot2('手写键盘')
    result = input_page.compare(pic_muzhi, pic)
    assert result == 0.0
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('26键')


@allure.story('麦克风权限默认禁止')
def test_InputMethod_SCB_Func_01_08_0001(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    # 进入华为手机系统设置页面
    os.system('adb -s %s shell am start com.android.settings/.HWSettings' %
              device_id_list[which_driver_pool])
    from page.base_page import BasePage
    base_page = BasePage(set_driver_pool)
    # 点击'设置'中的应用
    base_page.scroll_syspage_to_find('//*[@resource-id="com.android.settings:id/main_content"]', '应用')
    # 点击应用页面中的应用管理
    base_page.click_syspage_app_management()
    # 寻找应用管理页面中的'光子输入法'
    base_page.scroll_syspage_to_find('//*[@resource-id="android:id/list"]', '光子输入法')
    # 点击'权限'
    base_page.click_syspage_app_info()
    # 若已禁止，则授予麦克风权限
    if base_page.is_element_exist('已禁止'):
        assert base_page.is_element_exist('麦克风')
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('space', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    assert input_page.is_element_exist('禁止')


@allure.story('点击设置，允许麦克风权限，进入语音键盘')
def test_InputMethod_SCB_Func_01_08_0005(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.long_press('space', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.find_element_by_text_click('禁止后不再提示')
    # 进入华为手机系统设置页面
    os.system('adb -s %s shell am start com.android.settings/.HWSettings' %
              device_id_list[which_driver_pool])
    from page.base_page import BasePage
    base_page = BasePage(set_driver_pool)
    # 点击'设置'中的应用
    base_page.scroll_syspage_to_find('//*[@resource-id="com.android.settings:id/main_content"]', '应用')
    # 点击应用页面中的应用管理
    base_page.click_syspage_app_management()
    # 寻找应用管理页面中的'光子输入法'
    base_page.scroll_syspage_to_find('//*[@resource-id="android:id/list"]', '光子输入法')
    # 点击'权限'
    base_page.click_syspage_app_info()
    # 若已禁止，则授予麦克风权限
    if base_page.is_element_exist('已禁止'):
        base_page.click_syspage_universal('麦克风')
        base_page.click_syspage_universal('仅使用期间允许')
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('space', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    # 通过语音页面中的控件'语言选择按键，双击选择键盘语言'判断当前页面是否是语音属入页面
    assert input_page.is_element_exist('语言选择按键，双击选择键盘语言')


@allure.story('语音功能入口')
def test_InputMethod_SCB_Func_01_08_0006(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    '''
        此处需改为华为短信页面
    '''
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 长按空格调出语音输入界面
    input_page.long_press('space', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.deal_sys_dialog('要允许光子输入法录制音频吗？', '允许')
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('space', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    pic_yuyin = PATH(os.getcwd() + "/testcase/TestResult/语音界面.png")
    pic = input_page.screenshot2('语音界面')
    result = input_page.compare(pic_yuyin, pic)
    assert result < 2


@allure.story('输入emoji，无异常')
def test_InputMethod_SCB_Func_01_09_0002(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.input_characters('emjo', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    time.sleep(3)
    input_page.input_characters('q', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print('text:', text)
    assert text == '😀'


@allure.story('使用编辑键盘时，键盘功能全部置灰')
def test_InputMethod_SCB_Func_02_02_02_0003(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.tap_menu()
    input_page.tap_adjust_size()
    pic_bianji = PATH(os.getcwd() + "/testcase/TestResult/编辑键盘.png")
    pic = input_page.screenshot2('编辑键盘')
    result = input_page.compare(pic_bianji, pic)
    assert result < 2


@allure.story('删除只有一种键盘布局的语言，该语言重新展示在可用语言列表中')
def test_InputMethod_SCB_Func_03_01_01_0002(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.tap_menu()
    time.sleep(1)
    input_page.tap_setting()
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.open_input_menu_search('阿斯图里亚斯文')
    language_num_1 = language_setting_page.get_list_total_num('//android.widget.ExpandableListView/android'
                                                              '.widget.LinearLayout')
    language_setting_page.uncheck_language_list('阿斯图里亚斯文')
    if language_setting_page.check_the_language_states('阿斯图里亚斯文') == 'false':
        print('取消：', language_setting_page.is_element_exist('删除语言按键，双击删除 阿斯图里亚斯文 语言'))
        assert language_setting_page.is_element_exist('删除语言按键，双击删除 阿斯图里亚斯文 语言')
    time.sleep(1)
    language_setting_page.delete_language('阿斯图里亚斯文')
    language_num_2 = language_setting_page.get_list_total_num('//android.widget.ExpandableListView/android'
                                                              '.widget.LinearLayout')
    print('num: ', int(language_num_1) - int(language_num_2))
    assert int(language_num_1) - int(language_num_2) == 1
    # language_setting_page.add_language_list2('阿斯图里亚斯文', 'ast')

    # language_setting_page.return_to_launcher()


@allure.story('进入语言页-键盘长按地球键')
def test_InputMethod_SCB_Func_03_01_01_0010(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    assert language_setting_page.is_element_exist('语言')
    # language_setting_page.return_to_launcher()


@allure.story('进入语言页-键盘点击Menu')
def test_InputMethod_SCB_Func_03_01_01_0011(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.tap_menu()
    input_page.tap_setting()
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    assert language_setting_page.is_element_exist('语言')
    # language_setting_page.return_to_launcher()


@allure.story('进入语言页-点击输入法桌面icon')
def test_InputMethod_SCB_Func_03_01_01_0012(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0008']['ohos'] % device_id_list[which_driver_pool])
    time.sleep(1)
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    assert language_setting_page.is_element_exist('语言')
    # language_setting_page.return_to_launcher()


@allure.story('切换系统语言-系统语言需添加马来语')
def test_InputMethod_SCB_Func_03_01_01_0013(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    os.system(test_adb_data['adb_01_01_01_0009']['language_setting'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.to_system_language_picker('语言和地区', '马来文')
    time.sleep(3)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('Lebih banyak bahasa...')
    time.sleep(1)
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    # 判断马来西亚语有勾选状态，以此来判断马来西亚语已添加至【添加语言】列表中
    assert language_setting_page.check_the_language_states('Bahasa Melayu (Malaysia)')
    os.system(test_adb_data['adb_01_01_01_0009']['language_setting'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 还原系统语言至中文
    input_page.to_system_language_picker('Bahasa dan kawasan', 'Cina Ringkas')


@allure.story('添加语言-同意隐私声明-连接WiFi')
def test_InputMethod_SCB_Func_03_01_01_0015(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    time.sleep(3)
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    # 添加南非荷兰语前，'添加语言'列表中 item 的数目
    before_add_language = language_setting_page.get_list_total_num('//android.widget.ExpandableListView/android'
                                                                   '.widget.LinearLayout')
    if language_setting_page.is_element_exist('添加语言按键，双击添加 南非荷兰文 语言'):
        language_setting_page.add_language_list2('南非荷兰文', 'af')
    time.sleep(3)
    # 添加南非荷兰语后，'添加语言'列表中 item 的数目，如果添加后的语言数目-添加前的语言数目=1，说明语言添加成功，在'添加语言'列表中
    after_add_language = language_setting_page.get_list_total_num('//android.widget.ExpandableListView/android.widget'
                                                                  '.LinearLayout')
    if int(after_add_language) - int(before_add_language) == 1:
        assert language_setting_page.check_the_language_states('南非荷兰文') == 'true'
        language_setting_page.back_to_previous_page()
        os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
        afrikaans_keyboard = PATH(os.getcwd() + "/testcase/TestResult/南非键盘.png")
        pic = input_page.screenshot2('南非键盘')
        result = input_page.compare(afrikaans_keyboard, pic)
        assert result < 2

    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('中文')


@allure.story('语言布局切换')
def test_InputMethod_SCB_Func_03_01_01_0025(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    time.sleep(3)
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.updata_layout2('英语 (美国)', 2)
    time.sleep(1)
    language_setting_page.back_to_previous_page()
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.input_characters('qwerty', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    assert text == 'qwertz '
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.screenshot_universal('layout', 2)
    # input_page.return_to_launcher()


@allure.story('存在多个已添加语言-停用单个语言')
def test_InputMethod_SCB_Func_03_01_01_0046(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    time.sleep(3)
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.uncheck_language_list('英语 (美国)')
    time.sleep(1)
    states = language_setting_page.check_the_language_states('英语 (美国)')
    assert states == 'false'
    time.sleep(1)
    language_setting_page.is_element_exist('//android.widget.ImageView[@content-desc="删除语言按键，双击删除 %s 语言"]'
                                           % '英语 (美国)')
    time.sleep(1)
    language_setting_page.back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    assert input_page.is_element_exist('英语 (美国)') is False


@allure.story('【添加语言】中被勾选语言<5-添加语言')
def test_InputMethod_SCB_Func_03_01_01_0053(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    time.sleep(3)
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.add_language_list2('德语', 'de')
    states = language_setting_page.check_the_language_states('德语')
    assert states == 'true'


@allure.story('【添加语言】中被勾选语言<5-启用单个语言')
def test_InputMethod_SCB_Func_03_01_01_0051(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    time.sleep(3)
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.add_language_list2('西班牙语', 'es')
    language_setting_page.add_language_list2('法语', 'fr')
    language_setting_page.add_language_list2('俄语', 'ru')
    language_setting_page.uncheck_language_list('西班牙语')
    language_setting_page.uncheck_language_list('法语')
    language_setting_page.uncheck_language_list('俄语')
    # uncheck_language_list方法其实是点击checkbox，未选中时，点击则显示选中状态
    language_setting_page.uncheck_language_list('德语')
    assert language_setting_page.check_the_language_states('德语') == 'true'
    time.sleep(1)
    language_setting_page.back_to_previous_page()
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.is_element_exist('德语') is True


@allure.story('检查语言列表搜索入口')
def test_InputMethod_SCB_Func_03_01_02_0001(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    # 通过命令的方式启动输入法
    os.system(test_adb_data['adb_01_01_01_0008']['ohos'] % device_id_list[which_driver_pool])
    time.sleep(1)
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.click_input_menu_search()
    # 检查搜索框中是否出现'Search'文案，与清空按钮
    if language_setting_page.is_element_exist('Search'):
        if language_setting_page.is_element_exist('清空按键，双击清空搜索框内容'):
            language_setting_page.input_characters('q', device_id_list[which_driver_pool], screen_size_list[0],
                                                   screen_size_list[1])
            text = language_setting_page.find_element_by_class("android.widget.EditText").text
            assert text == '去'


@allure.story('检查搜索语言逻辑及功能')
def test_InputMethod_SCB_Func_03_01_02_0006(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.tap_menu()
    input_page.tap_setting()
    from page.keyboard_setting_page import KeyboardSettingPage
    KeyboardSettingPage(set_driver_pool).to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.click_input_menu_search()
    # 检查搜索框中是否出现'Search'文案，与清空按钮
    if language_setting_page.is_element_exist('Search'):
        if language_setting_page.is_element_exist('清空按键，双击清空搜索框内容'):
            input_page = InputPage(set_driver_pool)
            input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                  screen_size_list[1])
            input_page.language_picker_list('English(United States)')
            input_page.input_characters('p', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            # 目的：点击 back 键，收起键盘
            # input_page.back_to_previous_page()
            # text = input_page.find_element_by_class("android.widget.EditText").text
            if language_setting_page.is_element_exist('Polski') is not True:
                print('当前页面不含Polski')
            input_page.input_characters('olski', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            if language_setting_page.is_element_exist('Polski') is True:
                print('当前页面含有Polski')
            # input_page.return_to_launcher()


@allure.story('emoji候选展示')
def test_InputMethod_SCB_Func_03_05_01_0001(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_setting()
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(set_driver_pool)
    input_setting_page = keyboard_setting_page.to_input_setting_page()
    if input_setting_page.check_item_status('启用表情符号预测') is not True:
        input_setting_page.click_which_item('启用表情符号预测')
    input_setting_page.back_to_previous_page()
    keyboard_setting_page.back_to_previous_page()
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.input_characters('apple', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    input_page.click_which_candidate(3)
    text = input_page.find_element_by_class("android.widget.EditText").text
    assert text == '#127822;'


@allure.story('快速插入联想词输入检查02')
def test_InputMethod_SCB_Func_03_05_02_0015(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_setting()
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(set_driver_pool)
    input_setting_page = keyboard_setting_page.to_input_setting_page()
    if input_setting_page.check_item_status('快速插入联想词') is not True:
        input_setting_page.click_which_item('快速插入联想词')
    input_setting_page.back_to_previous_page()
    keyboard_setting_page.back_to_previous_page()
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.input_characters('test', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    # 获取 top1 的候选词
    top_1 = input_page.find_candidate(2)
    input_page.input_characters('space', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    # 查询 top1 的词是否在上屏的 text 中，如果在，则说明 test 上屏后，点击空格候选词也自动上屏
    assert top_1 in text


@allure.story('应用支持URL快捷键')
def test_InputMethod_SCB_Func_03_05_02_0015(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    # os.system(test_adb_data['adb_01_01_01_0010']['opera_browser'] % device_id_list[which_driver_pool])
    # time.sleep(1)
    # input_page.click_browser_search_box('Opera')
    # time.sleep(2)
    os.system(test_adb_data['adb_01_01_01_0011']['chrome_browser'] % device_id_list[which_driver_pool])
    time.sleep(1)
    input_page.click_browser_search_box('Chrome')
    time.sleep(3)
    if input_page.is_element_exist('com.kika.photon.inputmethod:id/extra_container_top'):
        pic = input_page.screenshot_urlboard('url')
        url_keyboard = PATH(os.getcwd() + "/testcase/TestResult/url.png")
        result = input_page.compare(url_keyboard, pic)
        assert result < 2
    input_page.click_url('url_www')
    input_page.click_url('url_point')
    input_page.click_url('url_slash')
    input_page.click_url('url_com')
    text = input_page.find_url_text('Chrome')
    assert text == 'www../.com​'
    input_page.click_url('left_layout')
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text2 = input_page.find_url_text('Chrome')
    assert text2 == 'www../.cm​'
    input_page.click_url('right_layout')
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                screen_size_list[1])
    text3 = input_page.find_url_text('Chrome')
    assert text3 == 'www../.c'
    # os.system(test_adb_data['adb_01_01_01_0012']['microsoft_browser'] % device_id_list[which_driver_pool])
    # time.sleep(2)
    # input_page.click_browser_search_box('MicroSoft')
    # time.sleep(2)
    # os.system(test_adb_data['adb_01_01_01_0013']['via_browser'] % device_id_list[which_driver_pool])
    # time.sleep(1)
    # input_page.click_browser_search_box('Via')
    # time.sleep(2)
    # os.system(test_adb_data['adb_01_01_01_0014']['firefox_browser'] % device_id_list[which_driver_pool])
    # time.sleep(1)
    # input_page.click_browser_search_box('FireFox')
    # time.sleep(2)


@allure.story('test')
def test_InputMethod_SCB_Func_test(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    input_page.to_which_keyboard_layout('手写键盘')
    time.sleep(2)
    # input_page.write_words()
    input_page.write_words()


@allure.story('打点测试，遍历 30 种键盘')
def test_30(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0008']['ohos'] % device_id_list[which_driver_pool])
    time.sleep(1)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(set_driver_pool)
    input_setting_page = keyboard_setting_page.to_input_setting_page()
    input_setting_page.click_which_item('快速插入联想词')
    input_setting_page.back_to_previous_page()
    keyboard_setting_page.to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.add_language_list2('马来文 (马来西亚)', 'ms_my')
    language_setting_page.add_language_list2('德文', 'de')
    language_setting_page.add_language_list2('英文 (澳大利亚)', 'en_AU')
    language_setting_page.add_language_list2('英文 (加拿大)', 'en_CA')
    language_setting_page.add_language_list2('英文 (英国)', 'en_GB')
    language_setting_page.add_language_list2('西班牙文', 'es')
    language_setting_page.add_language_list2('西班牙文（拉丁美洲）', 'es_la')
    # language_setting_page.add_language_list2('西班牙文 (美国)', 'es_us')
    language_setting_page.add_language_list2('西班牙文 (墨西哥)', 'es_mx')
    language_setting_page.add_language_list2('法文', 'fr')
    language_setting_page.add_language_list2('法文 (加拿大)', 'fr_ca')
    language_setting_page.add_language_list2('印度尼西亚文', 'id')
    language_setting_page.add_language_list2('意大利文', 'it')
    language_setting_page.add_language_list2('波兰语', 'pl')
    language_setting_page.add_language_list2('葡萄牙文 (巴西)', 'pt_br')
    language_setting_page.add_language_list2('葡萄牙文 (葡萄牙)', 'pt_pt')
    language_setting_page.add_language_list2('土耳其文', 'tr')
    language_setting_page.add_language_list2('捷克文', 'cs')
    language_setting_page.add_language_list2('俄文', 'ru')
    # language_setting_page.add_language_list2('乌尔都文', 'ur')
    language_setting_page.add_language_list2('阿拉伯文', 'ar')
    language_setting_page.add_language_list2('阿拉伯文 (阿尔及利亚)', 'ar_ar')
    language_setting_page.add_language_list2('阿拉伯文(黎凡特)', 'ar_li')
    language_setting_page.add_language_list2('阿拉伯文 (摩洛哥)', 'ar_mo')
    language_setting_page.add_language_list2('阿拉伯文 (沙特阿拉伯)', 'ar_sa')
    language_setting_page.add_language_list2('阿拉伯文 (突尼斯)', 'ar_tu')
    language_setting_page.add_language_list2('阿拉伯文 (埃及)', 'ar_eg')
    language_setting_page.add_language_list2('印地文', 'hi')
    language_setting_page.add_language_list2('泰文', 'th')
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    # 拉起键盘
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])

    input_page = InputPage(set_driver_pool)
    input_page.deal_sys_dialog('通讯录', '允许')
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    language_list = ['ไทย', 'हिन्दी', 'العربية (مصر)', 'العربية (تونس)', 'العربية (المملكة العربية السعودية)',
                     'العربية (المغرب)', 'العربية (الشرق)‎', 'العربية (الجزائر)', 'العربية', 'Русский',
                     'Čeština', 'Türkçe', 'Português (Portugal)', 'Português (Brasil)', 'Polski', 'Melayu (Malaysia)',
                     'Italiano', 'Indonesia', 'Français (Canada)', 'Français', 'Español(México)',
                     'Español(América Latina)', 'Español', 'English(United States)',
                     'English(United Kingdom)', 'English(Canada)', 'English(Australia)', 'Deutsch']
    # language_list = ['हिन्दी', 'العربية (مصر)', 'Deutsch']
    for language in language_list:
        # if language in ['العربية (مصر)', 'العربية (تونس)', 'العربية (المملكة العربية السعودية)',
        #              'العربية (المغرب)', 'العربية (الشرق)‎', 'العربية (الجزائر)', 'العربية', 'اردو']:
        # 点击语言键

        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        print('abc')
        time.sleep(1)
        input_page.language_picker_list(language)
        os.system('adb shell input tap 540 1800')
        os.system('adb shell input tap 540 1800')
        # 点击删除键
        input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        # 点击空格键
        input_page.input_characters('space', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        os.system('adb shell input tap 540 1800')
        # 点击回车键
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

        input_page.tap_menu()
        input_page.tap_keyboard_mode()
        input_page.to_which_keyboard_mode('单手模式')
        input_page.tap_menu()
        input_page.tap_keyboard_mode()
        input_page.to_which_keyboard_mode('悬浮键盘')
        input_page.tap_menu()
        input_page.tap_keyboard_mode()
        input_page.to_which_keyboard_mode('拇指模式')
        input_page.tap_menu()
        input_page.tap_keyboard_mode()
        input_page.to_which_keyboard_mode('编辑键盘')
        input_page.float_restore_default()
        input_page.tap_menu()
        input_page.tap_keyboard_mode()
        input_page.to_which_keyboard_mode('普通键盘')
        input_page.tap_menu()
        input_page.tap_keyboard_layout()
        list_num = input_page.get_list_total_num('//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view'
                                                 '"]/android.widget.LinearLayout')
        for i in range(1, list_num):
            text = input_page.find_element_by_xpath(
                '//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view"]/android.widget.LinearLayout['
                '%d]/android.widget.TextView' % (
                        1 + i)).get_attribute('text')
            if text == 'Dvorak':
                golVar.set_value('language_layout', 'relative_layout_dvorak')
            else:
                golVar.set_value('language_layout', 'relative_layout_en')
            input_page.find_element_by_xpath_click('//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view'
                                                   '"]/android.widget.LinearLayout[%d]' % (1+i))
            time.sleep(1)
            os.system('adb shell input tap 540 1800')
            os.system('adb shell input tap 540 1800')
            # 点击删除键
            input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            # 点击空格键
            input_page.input_characters('space', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            os.system('adb shell input tap 540 1800')
            # 点击回车键
            input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                        screen_size_list[1])
            input_page.tap_menu()
            input_page.tap_keyboard_layout()
        input_page.find_element_by_xpath_click(
            '//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view"]/android.widget.LinearLayout[1]')
    # 收起键盘
    input_page.menu_back()

@allure.story('打点测试，遍历 30 种键盘')
def test_31(get_device_id_list, set_driver_pool, cmdopt):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(cmdopt)
    input_page = InputPage(set_driver_pool)
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('单手模式')
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('悬浮键盘')
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('拇指模式')
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('编辑键盘')
    input_page.float_restore_default()
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('普通键盘')
    input_page.tap_menu()
    input_page.tap_keyboard_layout()
    list_num = input_page.get_list_total_num('//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view"]/android.widget.LinearLayout')
    print('list_num:', list_num)
    for i in range(1, list_num):
        text = input_page.find_element_by_xpath(
            '//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view"]/android.widget.LinearLayout[%d]/android.widget.TextView' % (
                        1 + i)).get_attribute('text')
        print(text)
        input_page.find_element_by_xpath_click('//*[@resource-id="com.kika.photon.inputmethod:id/recycler_view"]/android.widget.LinearLayout[%d]' % (1+i))

        input_page.tap_menu()
        input_page.tap_keyboard_layout()


if __name__ == '__main__':
    golVar.__init__()
    pytest.main()
