import json
import math
import operator
import os
import re
import time
from functools import reduce

import numpy
from PIL import ImageChops
from PIL.Image import Image, new
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import golVar
from commons.get_path import get_path, get_path_data
from util.log_info import Log_info
import time
import os
from PIL import ImageFile
from PIL import Image
import math
import operator

ImageFile.LOAD_TRUNCATED_IMAGES = True
PATH = lambda p: os.path.abspath(p)

test_case_data = get_path_data('/data/case_data.yml')
test_adb_data = get_path_data('/data/adb_data.yml')


class BaseFunction:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        print(driver)

    # 判断元素是否存在
    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    # 寻找元素集
    def find_elements(self, locator):
        try:
            return self.driver.find_elements(*locator)
        except:
            self.handle_exception('find_elements')

    # 寻找元素
    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception('find_element')

    # 通过滑动的方式寻找text
    def move_to_find_text(self, text):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
            '.text("%s").instance(0))' % text)

    # 定位到元素后，进行点击操作
    def find_element_click(self, locator):
        try:
            return self.find_element(locator).click()
        except:
            self.handle_exception('find_element_click')

    def handle_exception(self, ex_type):
        Log_info().getlog(ex_type).debug(self)

    # 通过text定位元素
    def find_element_by_text(self, text):
        try:
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text)
        except:
            self.handle_exception('find_element_by_text')

    # 通过text定位元素并点击
    def find_element_by_text_click(self, text):
        try:
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text).click()
        except:
            self.handle_exception('find_element_by_text_click')

    # 通过contenet-des定位元素
    def find_element_by_contenet_des(self, contenet):
        try:
            return self.driver.find_element_by_android_uiautomator('new UiSelector().description("%s")' % contenet)
        except:
            self.handle_exception('find_element_by_contenet')

    # 通过contenet-des定位元素并点击
    def find_element_by_contenet_des_click(self, contenet):
        try:
            return self.driver.find_element_by_android_uiautomator(
                'new UiSelector().description("%s")' % contenet).click()
        except:
            self.handle_exception('find_element_by_contenet_click')

    # 通过className定位元素
    def find_element_by_class(self, class_name):
        try:
            return self.driver.find_element_by_class_name(class_name)
        except:
            self.handle_exception('find_element_by_class')

    # 通过className定位元素
    def find_element_by_class_click(self, class_name):
        try:
            return self.driver.find_element_by_class_name(class_name).click()
        except:
            self.handle_exception('find_element_by_class_click')

    # 通过 id 寻找元素
    def find_element_by_id(self, id_name):
        try:
            return self.driver.find_element_by_id(id_name)
        except:
            self.handle_exception('find_element_by_id')

    # 通过 id 寻找元素并点击
    def find_element_by_id_click(self, id_name):
        try:
            return self.driver.find_element_by_id(id_name).click()
        except:
            self.handle_exception('find_element_by_id_click')

    # 通过 xpath 寻找元素
    def find_element_by_xpath(self, xpath_name):
        try:
            return self.driver.find_element_by_xpath(xpath_name)
        except:
            self.handle_exception('find_element_by_xpath')

    # 通过 xpath 寻找元素并点击
    def find_element_by_xpath_click(self, xpath_name):
        try:
            return self.driver.find_element_by_xpath(xpath_name).click()
        except:
            self.handle_exception('find_element_by_xpath_click')

    _gdpr_agree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_ok')
    _gdpr_disagree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_deny')
    _gdpr_learn_more_button = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_content2')

    # 点击键盘按键
    def click_keys(self, words, keys_list, device_id, screen_size_width, screen_size_height):
        for key_info in keys_list:
            if words == key_info['code']:
                os.system(test_adb_data['adb_01_01_01_0006']['shortclick'] % (
                    device_id, str(float(key_info['x']) * float(screen_size_width)),
                    str(float(key_info['y']) * float(screen_size_height))))
                print(str(float(key_info['x']) * float(screen_size_width)),
                      str(float(key_info['y']) * float(screen_size_height)))

    # 输入字符
    def input_characters(self, words, device_id, screen_size_width, screen_size_height):
        if len(words) != 0:
            language_layout = golVar.get_value('language_layout')
            print('language_layout:', language_layout)
            relative_layout_data_path = get_path('/layout/%s' % language_layout)
            with open(relative_layout_data_path) as file:
                keys_data = json.loads(file.read())
                keys_list = keys_data['keys']
                print(keys_list, type(keys_list))
            if (words == 'space') | (words == 'symbol') | (words == 'quotation') | (words == 'enter') | (
                    words == 'delete') | (words == 'shift') | (words == 'switch') | (words == 'emjo'):
                self.click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            elif words == ',':
                self.click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            elif words == '.':
                self.click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            else:
                for i in words:
                    self.click_keys(i, keys_list, device_id, screen_size_width, screen_size_height)
                time.sleep(1)
                self.click_keys('space', keys_list, device_id, screen_size_width, screen_size_height)

    # 点击候选词
    def click_candidate(self, click_actions, device_id, screen_size_width, screen_size_height):
        candidate_data_path = get_path('/layout/candidate_layout')
        with open(candidate_data_path) as file:
            candidate_coordinate_data = json.loads(file.read())
            candidate_coordinate_list = candidate_coordinate_data['keys']
            for candidate in candidate_coordinate_list:
                if click_actions == candidate['code']:
                    os.system(
                        test_adb_data['adb_01_01_01_0006']['shortclick'] %
                        (device_id, str(float(candidate['x']) * float(screen_size_width))
                         , str(float(candidate['y']) * float(screen_size_height))))
                    print(candidate['x'] * screen_size_width
                          , candidate['y'] * screen_size_height)

    def click_keyboard_menu(self, menu, device_id, screen_size_width, screen_size_height):
        relative_layout_data_path = get_path('/layout/menu_layout')
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
        os.system(test_adb_data['adb_01_01_01_0002']['deltext'] % device_id)

    # 清空已有内容
    def editClear(self, text1):
        # 123代表光标移动到末尾
        self.driver.keyevent(123)
        for z in range(0, len(text1)):
            # 67退格键
            self.driver.keyevent(67)

    def long_click_keys(self, words, keys_list, device_id, screen_size_width, screen_size_height):
        for key_info in keys_list:
            if words == key_info['code']:
                print(key_info['x'], key_info['y'])
                os.system(test_adb_data['adb_01_01_01_0007']['longclick'] %
                          (device_id, str(float(key_info['x']) * float(screen_size_width)),
                           str(float(key_info['y']) * float(screen_size_height)),
                           str(float(key_info['x']) * float(screen_size_width)),
                           str(float(key_info['y']) * float(screen_size_height))))

                print(str(float(key_info['x']) * float(screen_size_width)),
                      str(float(key_info['y']) * float(screen_size_height))
                      , str(float(key_info['x']) * float(screen_size_width)),
                      str(float(key_info['y']) * float(screen_size_height)))

    # 长按元素
    def long_press(self, words, device_id, screen_size_width, screen_size_height):
        if len(words) != 0:
            language_layout = golVar.get_value('language_layout')
            print('language_layout:', language_layout)
            relative_layout_data_path = get_path('/layout/%s' % language_layout)
            with open(relative_layout_data_path) as file:
                keys_data = json.loads(file.read())
                keys_list = keys_data['keys']
                print(keys_list, type(keys_list))
            if (words == 'space') | (words == 'symbol') | (words == 'quotation') | (words == 'enter') | (
                    words == 'delete') | (words == 'shift') | (words == 'switch') | (words == 'emjo'):
                self.long_click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            elif words == ',':
                self.long_click_keys('symbol', keys_list, device_id, screen_size_width, screen_size_height)
                self.long_click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
                self.long_click_keys('symbol', keys_list, device_id, screen_size_width, screen_size_height)
            elif words == '.':
                self.long_click_keys(words, keys_list, device_id, screen_size_width, screen_size_height)
            else:
                for i in words:
                    self.long_click_keys(i, keys_list, device_id, screen_size_width, screen_size_height)
                time.sleep(1)
                self.long_click_keys('space', keys_list, device_id, screen_size_width, screen_size_height)

    # tap封装
    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        # screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        # screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        # a = (float(x) / screen_width) * screen_width
        # x1 = int(a)
        # b = (float(y) / screen_height) * screen_height
        # y1 = int(b)
        # self.driver.tap([(x1, y1), (x1, y1)], duration)
        self.driver.tap([(x, y), (x, y)], duration)

    # 截图对比
    def screenshot(self, name):
        path = PATH(os.getcwd() + "/TestResult")
        if not os.path.isdir(PATH(os.getcwd() + "/TestResult")):
            os.makedirs(path)
        os.popen("adb wait-for-device")
        time.sleep(1)  # 由于多次出现截图延迟现象（每次截图都截的是上次操作的画面），故此处设置一个等待
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        time.sleep(1)
        os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + name + '_tmp.png'))
        # os.popen("adb pull /data/local/tmp/tmp1.png " + PATH('/Users/xm210407/PycharmProjects/Kika/testcase/'))
        time.sleep(1)
        os.popen("adb shell rm /data/local/tmp/tmp.png")
        time.sleep(1)
        im = Image.open(PATH(path + "/" + name + '_tmp.png'))
        cropedIm = im.crop((0, 1020, 1079, 2200))
        cropedIm.save(PATH(path + "/" + name + '_tmp.png'))
        return PATH(path + "/" + name + '_tmp.png')

    # 截图对比
    def screenshot2(self, name):
        path = PATH(os.getcwd() + "/TestResult")
        if not os.path.isdir(PATH(os.getcwd() + "/TestResult")):
            os.makedirs(path)
        os.popen("adb wait-for-device")
        time.sleep(1)  # 由于多次出现截图延迟现象（每次截图都截的是上次操作的画面），故此处设置一个等待
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        time.sleep(1)
        os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + name + '_tmp.png'))
        time.sleep(1)
        os.popen("adb shell rm /data/local/tmp/tmp.png")
        time.sleep(1)
        im = Image.open(PATH(path + "/" + name + '_tmp.png'))
        if self.is_element_exist('resource-id="com.huawei.ohos.inputmethod:id/scale_view'):
            crop_bounds = self.container_bounds('scale_view', 'resource_id')
        else:
            crop_bounds = self.container_bounds('keyboard_main_view', 'resource_id')
        cropedIm = im.crop((crop_bounds[0], crop_bounds[1], crop_bounds[2], crop_bounds[3]))
        cropedIm.save(PATH(path + "/" + name + '_tmp.png'))
        return PATH(path + "/" + name + '_tmp.png')

    def compare(self, pic1, pic2):
        '''
        :param pic1: 图片1路径
        :param pic2: 图片2路径
        :return: 返回对比的结果
        '''
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        print(differ)
        if differ < 2:
            print("应用成功")
        else:
            print("应用失败")
        return differ
    '''
    def compare2(self, image, target):
        
        :param pic1: 图片1路径
        :param pic2: 图片2路径
        :return: 返回对比的结果
        
        image = r'c:\temp\1.jpg'
        # target = r'c:\temp\2.jd03a4b21edd545812af46e7f84cc.jpg'
        target = r'c:\temp\Download-HD-Bamboo-Wallpapers.jpg'
        # target = r'c:\temp\Free-HD-Bamboo-Wallpapers-Download.jpg'
        img_gray = cv2.imread(target, cv2.IMREAD_GRAYSCALE)
        tImg = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        h, w = tImg.shape[:2]
        h0 = h // 4
        h1 = h - h // 4
        w0 = w // 4
        w1 = w - w // 4
        template = tImg[h0:h1, w0:w1]
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = numpy.where(res >= threshold)
        print(loc)
        if len(loc[0]):
            print("True")
        else:
            print("False")
    '''
    # 滑动方法
    def swipeUp(self, driver, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, driver, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, driver, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.8
        x2 = l['width'] * 0.25
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, driver, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

    def container_bounds(self, resource, which_type):
        if which_type == 'resource_id':
            locate_container_bounds = self.find_element_by_xpath(
                '//*[@resource-id="com.huawei.ohos.inputmethod:id/%s"]' % resource).get_attribute('bounds')
        if which_type == 'xpath':
            locate_container_bounds = self.driver.find_element_by_xpath('//*[@text="%s"]/following-sibling::android'
                                                                        '.widget.SeekBar' % resource).get_attribute(
                'bounds')
        container_bounds_string_to_array = re.findall(r'\d+', locate_container_bounds)
        container_sx, container_sy, container_ex, container_ey = float(container_bounds_string_to_array[0]), \
                                                                 float(container_bounds_string_to_array[1]), \
                                                                 float(container_bounds_string_to_array[2]), \
                                                                 float(container_bounds_string_to_array[3])
        return container_sx, container_sy, container_ex, container_ey

    def back_to_previous_page(self):
        self.driver.back()
