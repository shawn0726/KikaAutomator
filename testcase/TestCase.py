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
1、python3 -m pytest testcase/noTestCase.py --alluredir report/allure_raw
2、allure generate report/allure_raw -o report/html --clean
'''

screen_size_list = []
test_case_data = get_path_data('/data/case_data.yml')
test_adb_data = get_path_data('/data/adb_data.yml')

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


@allure.story('检查删除键功能')
# 通过 case_number 在 case_id 表中查询，对应的 case 使用哪个 driver
def test_InputMethod_SCB_func_01_01_01_0001(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_0002(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_0003(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_0008(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_0009(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_00010(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_setting().to_page_setting_page().check_bubble_capitalization('noselect')
    from page.page_setting_page import PageSettingPage
    PageSettingPage(set_driver_pool).back_to_setting_page().back_to_input_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('更多语言...')
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(set_driver_pool)
    language_setting_page.uncheck_language_list('中文')
    language_setting_page.back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('qwertyuiopasdfghjklzxcvbnm', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == '1234567890@#$%&-+()*\"\':;!?'


@allure.story('检查空格键功能使用')
def test_InputMethod_SCB_func_01_01_01_00011(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_00013(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.long_press('space', device_id_list[which_driver_pool],
                          screen_size_list[0], screen_size_list[1])
    input_page.deal_sys_dialog('要允许小艺输入法录制音频吗？', '允许')
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('space', device_id_list[which_driver_pool],
                          screen_size_list[0], screen_size_list[1])
    assert input_page.is_element_exist('语言选择按键，双击选择键盘语言') is True


@allure.story('检查句号长按弹泡功能')
def test_InputMethod_SCB_func_01_01_01_00016(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_01_01_00036(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    # 26键点击中/英切换键
    # 英文键盘
    pic_26_english = input_page.screenshot2('26键英文')
    pic_26_english_path = PATH(os.getcwd() + "/TestResult/26键英文.png")
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
    pic_26_chinese_path = PATH(os.getcwd() + "/TestResult/26键中文.png")
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
    pic_9_path = PATH(os.getcwd() + "/TestResult/9键中文.png")
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
    pic_bihua_path = PATH(os.getcwd() + "/TestResult/笔画中文.png")
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
    pic_shouxie_path = PATH(os.getcwd() + "/TestResult/手写中文.png")
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
    language_setting_page.add_language_list('中文', 'zh_HK')
    language_setting_page.add_language_list('中文', 'zh_TW')
    language_setting_page.back_to_previous_page()
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    golVar.set_value('language_layout', '注音')
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    # 添加注音键盘
    input_page.language_picker_list('中文（注音）')
    pic_zhuyin = input_page.screenshot2('注音中文')
    pic_zhuyin_path = PATH(os.getcwd() + "/TestResult/注音中文.png")
    result_zhuyin = input_page.compare(pic_zhuyin_path, pic_zhuyin)
    pytest.assume(result_zhuyin == 0.0)
    # 添加仓颉键盘
    # golVar.set_value('language_layout', '仓颉')
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    input_page.language_picker_list('中文（倉頡）')
    pic_cangjie = input_page.screenshot2('倉頡中文')
    pic_cangjie_path = PATH(os.getcwd() + "/TestResult/倉頡中文.png")
    result_cangjie = input_page.compare(pic_cangjie_path, pic_cangjie)
    pytest.assume(result_cangjie == 0.0)


@allure.story('单手键盘初始状态和基础功能检查')
def test_InputMethod_SCB_func_01_02_0003(get_device_id_list, set_driver_pool, cmdopt):
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
    os.system('adb -s %s shell pm clear com.huawei.ohos.inputmethod' % device_id_list[which_driver_pool])
    input_page.set_default_inputmethod('ziyan')
    time.sleep(3)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
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
def test_InputMethod_SCB_func_01_03_0010(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_01_04_0002(get_device_id_list, set_driver_pool, cmdopt):
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
    os.system('adb -s %s shell pm clear com.huawei.ohos.inputmethod' % device_id_list[which_driver_pool])
    input_page.set_default_inputmethod('ziyan')
    time.sleep(5)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.deal_gdpr_informal()
    time.sleep(5)
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.tap_menu()
    input_page.tap_keyboard_mode()
    input_page.to_which_keyboard_mode('拇指模式')
    pic_muzhi = PATH(os.getcwd() + "/TestResult/拇指键盘.png")
    pic = input_page.screenshot2('拇指键盘')
    result = input_page.compare(pic_muzhi, pic)
    assert result == 0.0


@allure.story('使用外接键盘输入字符能够正常展示')
def test_InputMethod_SCB_func_01_05_0005(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
        外界键盘？？？
    '''


@allure.story('显示一元联想词语言确认')
def test_InputMethod_SCB_func_01_05_0034(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
            外界键盘？？？
    '''


@allure.story('简体中文支持手写键盘')
def test_InputMethod_SCB_func_01_07_0001(get_device_id_list, set_driver_pool, cmdopt):
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
    pic_muzhi = PATH(os.getcwd() + "/TestResult/手写中文.png")
    pic = input_page.screenshot2('手写键盘')
    result = input_page.compare(pic_muzhi, pic)
    assert result == 0.0


@allure.story('麦克风权限默认禁止')
def test_InputMethod_SCB_func_01_08_0001(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
            进入系统设置-应用管理，查看以禁止的应用，只能用华为手机写case，其他品牌路径不同
    '''


@allure.story('点击设置，允许麦克风权限，进入语音键盘')
def test_InputMethod_SCB_func_01_08_0005(get_device_id_list, set_driver_pool, cmdopt):
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
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    '''
            进入系统设置-应用管理，查看以禁止的应用，只能用华为手机写case，其他品牌路径不同
    '''


@allure.story('语音功能入口')
def test_InputMethod_SCB_func_01_08_0006(get_device_id_list, set_driver_pool, cmdopt):
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
    input_page.deal_sys_dialog('要允许小艺输入法录制音频吗？', '允许')
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    input_page.long_press('space', device_id_list[which_driver_pool], screen_size_list[0],
                          screen_size_list[1])
    pic_yuyin = PATH(os.getcwd() + "/TestResult/语音界面.png")
    pic = input_page.screenshot2('语音界面')
    result = input_page.compare(pic_yuyin, pic)
    assert result < 2


@allure.story('输入emoji，无异常')
def test_InputMethod_SCB_func_01_09_0002(get_device_id_list, set_driver_pool, cmdopt):
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
def test_InputMethod_SCB_func_02_02_02_0003(get_device_id_list, set_driver_pool, cmdopt):
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
    pic_bianji = PATH(os.getcwd() + "/TestResult/编辑键盘.png")
    pic = input_page.screenshot2('编辑键盘')
    result = input_page.compare(pic_bianji, pic)
    assert result < 2


@allure.story('删除只有一种键盘布局的语言，该语言重新展示在可用语言列表中')
def test_InputMethod_SCB_func_03_01_01_0002(get_device_id_list, set_driver_pool, cmdopt):
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
    language_setting_page.uncheck_language_list('阿斯图里亚斯文')
    time.sleep(1)
    language_setting_page.delete_language('阿斯图里亚斯文')
    language_setting_page.add_language_list('阿斯图里亚斯文', 'ast')


if __name__ == '__main__':
    golVar.__init__()
    pytest.main()
