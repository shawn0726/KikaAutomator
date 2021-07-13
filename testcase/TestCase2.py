import re
import time
from multiprocessing import Pool
import os

import allure
from selenium.webdriver.common.by import By
import yaml

from page.app import App
from commons.start_service import start_appium
from page.app import App
from util.device_data import get_vm_size, keep_port_available
from util.log_info import Log_info

'''
生成allure报告 2 步：
1、python3 -m pytest testcase/TestCase.py --alluredir report/allure_raw
2、allure generate report/allure_raw -o report/html --clean
'''


device_id_list = []
desired_process = []
screen_size_list = []
script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_data_path = script_path_up + '/data/case_data.yml'
test_case_data = yaml.safe_load(open(case_data_path, 'r'))


@allure.feature('测试')
class TestCase:
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

    def setup(self):
        print("se-up")
        # device_info = os.popen('adb devices').read()
        device_id_list.clear()
        from commons import start_service
        list1 = start_service.start_devices()
        for i in range(len(list1)):
            device_id_list.append(list1[i])
        device_id_list_num = len(device_id_list)
        port_id = 4724
        bp_id = 99
        sys_port = 8200
        if device_id_list_num != 0:
            p = Pool(device_id_list_num)
            print(p)

            for i in range(device_id_list_num):
                port_id = port_id + 1
                bp_id = bp_id + 1
                sys_port = sys_port + 1
                # port_available = os.popen('lsof -i tcp:%d' % port_id).read()
                # pid = re.findall(r'(\s\d+\s)', port_available)
                # port_available_last = ''.join(pid).strip()
                # try:
                #     os.system('kill %s' % port_available_last)
                # except Exception as e:
                #     Log_info().getlog('kill-port').debug(e)
                keep_port_available(port_id)
                try:
                    p.apply_async(start_appium, args=(port_id, bp_id, device_id_list[i],))
                except Exception as e:
                    Log_info().getlog('start-appium-test-case').debug(e)
                # wait(10)
                time.sleep(3)
                try:
                    self.input_page = App.start(self, port_id,
                                                device_id_list[i],
                                                sys_port).set_default_method().agree_gdpr().back_to_input_page()
                except Exception as e:
                    # print('c')
                    Log_info().getlog('start-drive-test-case').debug(e)
                time.sleep(2)
                screen_size_list.clear()
                # vm_size = os.popen('adb -s %s shell wm size' % device_id_list[i]).read()
                # print(vm_size, type(vm_size))
                # vm_size_list = re.findall(r'([0-9]\d*\d*[0-9])', vm_size)
                # width = vm_size_list[0]
                # screen_size_list.append(width)
                # height = vm_size_list[1]
                # screen_size_list.append(height)
                get_vm_size(device_id_list[i], screen_size_list)

                print(screen_size_list[0], screen_size_list[1])

                # self.input_page.deal_gdpr(self._gdpr_pop_up, 'agree')
                # _thread.start_new_thread(start_appium, (port_id, bp_id, device_id_list[i],))
            p.close()
            p.terminate()

        return device_id_list


    @allure.story('英文键盘，输字母后删除')
    def test_InputMethod_SCB_func_01_01_01_0001(self):
        # device_id_list = start_service.start_devices()
        print('----- %s -----' % device_id_list)
        device_id_list_num = len(device_id_list)
        for i in range(device_id_list_num):
            os.system('adb -s %s shell am start -S com.xinmei365.emptyinput/.MainActivity' % device_id_list[i])
            time.sleep(1)
            os.system('adb -s %s shell input tap 500 500' % device_id_list[i])
            time.sleep(3)
            # self.input_page.implicitly_wait(3)
            # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
            if self.input_page.check_language(device_id_list[i], screen_size_list[0], screen_size_list[1]) == 'english':
                print('当前为英文键盘')
            else:
                self.input_page.input_characters('switch', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('enter', device_id_list[i], screen_size_list[0], screen_size_list[1])

            self.input_page.input_characters(test_case_data['func_01_01_01_0001']['word1'], device_id_list[i],
                                             screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters(',', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters(test_case_data['func_01_01_01_0001']['word2'], device_id_list[i],
                                             screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('delete', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('delete', device_id_list[i], screen_size_list[0], screen_size_list[1])
        text = self.input_page.find_element_by_class("android.widget.EditText").text
        print(text)
        assert text == 'hello ,worl'

    @allure.story('检查首字母大写功能')
    def test_InputMethod_SCB_func_01_01_01_0003(self):
        device_id_list_num = len(device_id_list)
        for i in range(device_id_list_num):
            os.system('adb -s %s shell am start -a android.intent.action.SENDTO -d sms:10086' % device_id_list[i])
            self.input_page.find_element_click(self._message_input_box)
            self.input_page.input_characters(test_case_data['func_01_01_01_0002']['word'], device_id_list[i],
                                             screen_size_list[0], screen_size_list[1])
        text = self.input_page.find_element_by_class("android.widget.EditText").text
        assert text == 'QWERT '

    def test_InputMethod_SCB_func_01_01_01_0008(self):
        device_id_list_num = len(device_id_list)
        for i in range(device_id_list_num):
            self.input_page.input_characters('qwert', device_id_list[i], screen_size_list[0], screen_size_list[1])
        text = self.input_page.find_element_by_class("android.widget.EditText").text
        if text == 'qwert ':
            self.input_page.input_characters('shift', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('shift', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('qwert', device_id_list[i], screen_size_list[0], screen_size_list[1])
            text2 = self.input_page.find_element_by_class("android.widget.EditText").text
            assert text2 == 'QWERT '
        else:
            self.input_page.input_characters('shift', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('shift', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('shift', device_id_list[i], screen_size_list[0], screen_size_list[1])
            self.input_page.input_characters('qwert', device_id_list[i], screen_size_list[0], screen_size_list[1])
            text3 = self.input_page.find_element_by_class("android.widget.EditText").text
            assert text3 == 'QWERT '

    def test_InputMethod_SCB_func_01_01_01_0009(self):
        device_id_list_num = len(device_id_list)
        for i in range(device_id_list_num):
            self.input_page.input_characters('abcdef', device_id_list[i], screen_size_list[0], screen_size_list[1])
        text4 = self.input_page.find_element_by_class("android.widget.EditText").text
        assert text4 == 'a b c d e f '

    def test_sp(self):
        # pass
        for i in range(len(device_id_list)):
            vm_size = os.popen('adb -s %s shell wm size' % device_id_list[i]).read()
            print(vm_size, type(vm_size))
            vm_size_list = re.findall(r'([0-9]\d*\d*[0-9])', vm_size)
            width = vm_size_list[0]
            print(width, type(width))
            height = vm_size_list[1]
            print(height, type(height))
