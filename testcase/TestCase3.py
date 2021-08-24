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
1、python3 -m pytest testcase/TestCase.py --alluredir report/allure_raw
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


if __name__ == '__main__':
    golVar.__init__()
    pytest.main(['-s', '-v', '-n=2', 'testcase/TestCase2.py'])
