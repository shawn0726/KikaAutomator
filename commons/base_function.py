import json
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from commons.get_path import get_path, get_path_data
from util.log_info import Log_info

test_case_data = get_path_data('/data/case_data.yml')
test_adb_data = get_path_data('/data/adb_data.yml')


class BaseFunction:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        print(driver)

    def elements_judge(self, locator):
        if len(self.find_elements(locator)) >= 1:
            return True
        else:
            return False

    def find_elements(self, locator):
        try:
            return self.driver.find_elements(*locator)
        except:
            self.handle_exception('find_elements')
            return self.driver.find_elements(*locator)

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception('find_elements')
            return self.driver.find_element(*locator)

    def find_element_click(self, locator):
        try:
            return self.find_element(locator).click()
        except:
            self.handle_exception('find_element_click')
            return self.find_element(locator).click()

    def handle_exception(self, ex_type):
        Log_info().getlog(ex_type).debug(self)

    # 通过text定位元素

    def find_element_by_text(self, text):
        try:
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text)
        except:
            self.handle_exception('find_element_by_text')

    def find_element_by_text_click(self, text):
        try:
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text).click()
        except:
            self.handle_exception('find_element_by_text_click')

    # 通过className定位元素

    def find_element_by_class(self, class_name):
        try:
            return self.driver.find_element_by_class_name(class_name)
        except:
            self.handle_exception('find_element_by_class')
            return self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/'
                                                     'android.widget.FrameLayout[2]/android.widget.RelativeLayout/'
                                                     'android.widget.EditText')

    def find_element_by_class_click(self, class_name):
        try:
            return self.driver.find_element_by_class_name(class_name).click()
        except:
            self.handle_exception('find_element_by_class_click')
            return self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/'
                                                     'android.widget.FrameLayout[2]/android.widget.RelativeLayout/'
                                                     'android.widget.EditText').click()

    def find_element_by_id(self, id_name):
        try:
            return self.driver.find_element_by_id(id_name)
        except:
            self.handle_exception('find_element_by_id')

    def find_element_by_id_click(self, id_name):
        try:
            return self.driver.find_element_by_id(id_name).click()
        except:
            self.handle_exception('find_element_by_id_click')

    _gdpr_agree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_ok')
    _gdpr_disagree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_deny')
    _gdpr_learn_more_button = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_content2')

    # @pytest.mark.parametrize('words', 'space')
    # @pytest.mark.parametrize('device_id', 'b0ebfef8')

    def click_keys(self, words, keys_list, device_id, screen_size_width, screen_size_height):
        for key_info in keys_list:
            if words == key_info['code']:
                # print(key_info['x'], key_info['y'])
                os.system(test_adb_data['adb_01_01_01_0006']['shortclick'] % (
                    device_id, str(float(key_info['x']) * float(screen_size_width)),
                    str(float(key_info['y']) * float(screen_size_height))))
                print(str(float(key_info['x']) * float(screen_size_width)),
                      str(float(key_info['y']) * float(screen_size_height)))
                return

    def input_characters(self, words, device_id, screen_size_width, screen_size_height):
        if len(words) != 0:
            # script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # relative_layout_data_path = script_path_up + '/layout/relative_layout_en'
            relative_layout_data_path = get_path('/layout/relative_layout_en')
            with open(relative_layout_data_path) as file:
                keys_data = json.loads(file.read())
                keys_list = keys_data['keys']
                print(keys_list, type(keys_list))
            if (words == 'space') | (words == 'symbol') | (words == 'quotation') | (words == 'enter') | (
                    words == 'delete') | (words == 'shift') | (words == 'switch'):
                self.click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            elif words == ',':
                # self.click_keys('symbol', keys_list, device_id, screen_size_width, screen_size_height)
                self.click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
                # self.click_keys('symbol', keys_list, device_id, screen_size_width, screen_size_height)
            elif words == '.':
                self.click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            else:
                for i in words:
                    # for key_info in keys_list:
                    #     if i == key_info['code']:
                    #         print(i, key_info['x'], key_info['y'])
                    #         os.system('adb -s %s shell input tap %d %d' % (device_id, key_info['x'], key_info['y']))
                    self.click_keys(i, keys_list, device_id, screen_size_width, screen_size_height)
                time.sleep(1)
                self.click_keys('space', keys_list, device_id, screen_size_width, screen_size_height)

    def click_candidate(self, click_actions, device_id, screen_size_width, screen_size_height):
        # script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # candidate_data_path = script_path_up + '/layout/candidate_layout'
        candidate_data_path = get_path('/layout/candidate_layout')
        with open(candidate_data_path) as file:
            candidate_coordinate_data = json.loads(file.read())
            candidate_coordinate_list = candidate_coordinate_data['keys']
            for candidate in candidate_coordinate_list:
                if click_actions == candidate['code']:
                    # print(candidate['x'], candidate['y'])
                    os.system(
                        test_adb_data['adb_01_01_01_0006']['shortclick'] %
                        (device_id, str(float(candidate['x']) * float(screen_size_width))
                         , str(float(candidate['y']) * float(screen_size_height))))
                    print(candidate['x'] * screen_size_width
                          , candidate['y'] * screen_size_height)

    def click_keyboard_menu(self, menu, device_id, screen_size_width, screen_size_height):
        # script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # menu_data_path = script_path_up + '/layout/menu_layout'
        relative_layout_data_path = get_path('/layout/relative_layout_en')
        with open(relative_layout_data_path) as file:
            menu_location_data = json.loads(file.read())
            menu_location = menu_location_data['key']
            for i in menu_location:
                if menu == 'Layout':
                    os.system(test_adb_data['adb_01_01_01_0006']['shortclick'] %
                              (device_id, str(float(i['x']) * float(screen_size_width))
                               , str(float(i['y']) * float(screen_size_height))))

    # 中英检查
    def check_language(self, device_id, screen_size_width, screen_size_height):
        words = 'q'
        self.input_characters(words, device_id, screen_size_width, screen_size_height)
        time.sleep(2)
        if self.find_element_by_class("android.widget.EditText").text == 'q':
            return 'english'
        else:
            return 'chinese'

    def return_to_launcher(self, device_id):
        # for i in range()

        os.system(test_adb_data['adb_01_01_01_0002']['deltext'] % device_id)

    #清空已有内容
    def editClear(self, text1):
        #123代表光标移动到末尾
        self.driver.keyevent(123)
        for z in range(0, len(text1)):
        #67退格键
         self.driver.keyevent(67)

    def long_click_keys(self, words, keys_list, device_id, screen_size_width, screen_size_height):
        for key_info in keys_list:
            if words == key_info['code']:
                print(key_info['x'], key_info['y'])
                os.system(test_adb_data['adb_01_01_01_0007']['longclick'] % (device_id,
                                                                           str(float(key_info['x']) * float(screen_size_width)),
                                                                           str(float(key_info['y']) * float(screen_size_height)),
                                                                           str(float(key_info['x']) * float(screen_size_width)),
                                                                           str(float(key_info['y']) * float(screen_size_height))))
                # os.system('adb -s %s shell input tap %s %s' % (device_id, str(float(key_info['x']) * float(screen_size_width)),
                #                                                str(float(key_info['y']) * float(screen_size_height))))
                # print(str(float(key_info['x']) * float(screen_size_width)),
                #                                                str(float(key_info['y']) * float(screen_size_height)))

                print(str(float(key_info['x']) * float(screen_size_width)),str(float(key_info['y']) * float(screen_size_height))
                      ,str(float(key_info['x']) * float(screen_size_width)),str(float(key_info['y']) * float(screen_size_height)))
                return

    # 长按元素
    def long_press(self, words, device_id, screen_size_width, screen_size_height):
        if len(words) != 0:
            relative_layout_data_path = get_path('/layout/relative_layout_en')
            with open(relative_layout_data_path) as file:
                keys_data = json.loads(file.read())
                keys_list = keys_data['keys']
                print(keys_list, type(keys_list))
            if (words == 'space') | (words == 'symbol') | (words == 'quotation') | (words == 'enter') | (
                    words == 'delete') | (words == 'shift') | (words == 'switch'):
                self.long_click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            elif words == ',':
                self.long_click_keys('symbol', keys_list, device_id, screen_size_width, screen_size_height)
                self.long_click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
                self.long_click_keys('symbol', keys_list, device_id, screen_size_width, screen_size_height)
            elif words == '.':
                self.long_click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            else:
                for i in words:
                    # for key_info in keys_list:
                    #     if i == key_info['code']:
                    #         print(i, key_info['x'], key_info['y'])
                    #         os.system('adb -s %s shell input tap %d %d' % (device_id, key_info['x'], key_info['y']))
                    print("_________" + i + "_________")
                    self.long_click_keys(i,keys_list, device_id, screen_size_width, screen_size_height)
                time.sleep(1)
                self.long_click_keys('space',keys_list, device_id, screen_size_width, screen_size_height)
    #tap封装
    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)


