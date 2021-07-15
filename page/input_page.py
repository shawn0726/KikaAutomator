import json
import os

from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction
from commons.get_path import get_path


class InputPage(BaseFunction):
    _xpath_locator_ohos = (
        By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    _id_locator_input_gdpr_agree = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_ok')
    _xpath_locator_menu = (By.XPATH, '//*[@resource-id="com.huawei.ohos.inputmethod:id/icon"]')
    _xpath_locator_sound_vibration = (By.XPATH, '//*[@text="音效和振动"]')

    '''
    inputPage 页面即键盘页面，键盘上层覆盖蒙层，无法通过元素属性定位，采取坐标方式；
    以下方式均为点击坐标的方式：Menu、Back、菜单页面功能菜单：键盘布局(0.157, 0.709)、键盘模式(0.379, 0.705)、主题(0.611, 0.704)、编辑键盘(0.839, 0.701)、剪切板(0.157, 0.829)、编辑(0.385, 0.825)、音效和振动(0.608, 0.83)、设置(0.842, 0.825)
    '''

    # 点击键盘左上角menu按钮进入menu菜单，
    def tap_menu(self, screen_size_width, screen_size_height):
        self.driver.tap([(str(0.078 * float(screen_size_width)), str(0.621 * float(screen_size_height)))])

    # 点击键盘右上角返回按钮
    def menu_back(self, screen_size_width, screen_size_height):
        self.driver.tap([(str(0.921 * float(screen_size_width)), str(0.621 * float(screen_size_height)))])

    # 点击menu页子菜单
    def to_which_submenu(self, which_one, screen_size_width, screen_size_height):
        menu_data_path = get_path('/layout/menu_layout')
        with open(menu_data_path) as file:
            menu_location_data = json.loads(file.read())
            menu_location = menu_location_data['keys']
            print('menu_location:%s' % menu_location)
        for submenu in menu_location:
            if submenu['code'] == which_one:
                if which_one == 'Theme':
                    self.driver.tap([(str(float(submenu['x']) * float(screen_size_width)),
                                      str(float(submenu['y']) * float(screen_size_height)))])
                    from page.theme_setting_page import ThemeSettingPage
                    return ThemeSettingPage(self.driver)
                elif which_one == 'Settings':
                    self.driver.tap([(str(float(submenu['x']) * float(screen_size_width)),
                                      str(float(submenu['y']) * float(screen_size_height)))])
                    from page.keyboard_setting_page import KeyboardSettingPage
                    return KeyboardSettingPage(self.driver)
                else:
                    self.driver.tap([(str(float(submenu['x']) * float(screen_size_width)),
                                      str(float(submenu['y']) * float(screen_size_height)))])
                    print((str(float(submenu['x']) * float(screen_size_width)),
                           str(float(submenu['y']) * float(screen_size_height))))

    # 切换键盘布局
    def to_which_keyboard_layout(self, which_one, screen_size_width, screen_size_height):
        pass

    # 更改键盘模式
    def to_which_keyboard_mode(self, which_one, screen_size_width, screen_size_height):
        menu_data_path = get_path('/layout/keyboard_mode_layout')
        with open(menu_data_path) as file:
            keyboard_mode_data = json.loads(file.read())
            keyboard_mode = keyboard_mode_data['keys']
        for mode in keyboard_mode:
            if mode['code'] == which_one:
                self.driver.tap([(str(float(mode['x']) * float(screen_size_width)),
                                  str(float(mode['y']) * float(screen_size_height)))])

    # 编辑键盘-调节尺寸大小
    def adjust_size(self):
        pass

    # 剪切板
    def clipboard_func(self, which_one, operating):
        pass

    # 编辑-全选、复制、粘贴、剪切板
    def edit(self, which_one, screen_size_width, screen_size_height):
        edit_data_path = get_path('/layout/edit_layout')
        with open(edit_data_path) as file:
            edit_location_data = json.loads(file.read())
            edit_location = edit_location_data['keys']
            print('menu_location:%s' % edit_location)
        for edit_key in edit_location:
            if edit_key['code'] == which_one:
                self.driver.tap([(str(float(edit_key['x']) * float(screen_size_width)),
                                  str(float(edit_key['y']) * float(screen_size_height)))])

    # 声音和振动菜单子页面，调整声音
    def adjust_sound(self, size, screen_size_width, screen_size_height):
        if size == 'max':
            self.driver.tap([(str(0.99 * float(screen_size_width)), str(0.861 * float(screen_size_height)))])
        if size == 'min':
            self.driver.tap([(str(0.01 * float(screen_size_width)), str(0.861 * float(screen_size_height)))])
        if size == 'middle':
            self.driver.tap([(str(0.5 * float(screen_size_width)), str(0.861 * float(screen_size_height)))])

    # 调整振动，目前支持最大、最小，中间调节
    def adjust_vibration(self, size, screen_size_width, screen_size_height):
        if size == 'max':
            self.driver.tap([(str(0.99 * float(screen_size_width)), str(0.746 * float(screen_size_height)))])
        if size == 'min':
            self.driver.tap([(str(0.01 * float(screen_size_width)), str(0.746 * float(screen_size_height)))])
        if size == 'middle':
            self.driver.tap([(str(0.5 * float(screen_size_width)), str(0.746 * float(screen_size_height)))])

    # 进入音量调节页面
    def enter_keyboard_sound_page(self, screen_size_width, screen_size_height):
        self.driver.tap([(str(0.5 * float(screen_size_width)), str(0.922 * float(screen_size_height)))])
        from page.theme_setting_page import ThemeSettingPage
        return ThemeSettingPage(self.driver)  # KeyboardSoundPage

    '''
    def tap_menu(self):
        # self.driver.find_element_by_xpath(self._xpath_locator_menu).click()
        self.find_element_click(self._xpath_locator_menu)

    def click_sound_vibration_menu(self):
        self.find_element_click(self._xpath_locator_sound_vibration)

    def adjust_vibration(self, size, screen_size_width, screen_size_height):
        if size == 'max':
            self.driver.tap([(str(0.9 * float(screen_size_width)), str(0.746 * float(screen_size_height)))])
        if size == 'min':
            self.driver.tap([(str(0.01 * float(screen_size_width)), str(0.746 * float(screen_size_height)))])
        if size == 'middle':
            self.driver.tap([(str(0.5 * float(screen_size_width)), str(0.746 * float(screen_size_height)))])
    '''
