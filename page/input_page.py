import json
import os

from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction


class InputPage(BaseFunction):
    _xpath_locator_ohos = (
        By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    _id_locator_input_gdpr_agree = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_ok')
    _xpath_locator_menu = (By.XPATH, '//*[@content-desc="菜单按键。双击打开菜单页面。"]')

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

    def to_which_submenu(self, which_one, screen_size_width, screen_size_height):
        script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        menu_data_path = script_path_up + '/layout/menu_layout'
        with open(menu_data_path) as file:
            menu_location_data = json.loads(file.read())
            menu_location = menu_location_data['key']
        for submenu in menu_location:
            if submenu == which_one:
                if which_one == 'keyboard_theme':
                    self.driver.tap([(str(float(menu_location['x']) * float(screen_size_width)),
                                      str(float(menu_location['x']) * float(screen_size_height)))])
                    from page.theme_page import ThemePage
                    return ThemePage(self.driver)
                elif which_one == 'keyboard_setting':
                    self.driver.tap([(str(float(menu_location['x']) * float(screen_size_width)),
                                      str(float(menu_location['x']) * float(screen_size_height)))])
                    from page.keyboard_setting_page import KeyboardSettingPage
                    return KeyboardSettingPage(self.driver)
            else:
                self.driver.tap([(str(float(menu_location['x']) * float(screen_size_width)),
                                  str(float(menu_location['x']) * float(screen_size_height)))])

    # 键盘布局
    def to_which_keyboard_layout(self, which_one, screen_size_width, screen_size_height):
        pass

    # 键盘模式
    def to_which_keyboard_mode(self, which_one, screen_size_width, screen_size_height):
        script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        menu_data_path = script_path_up + '/layout/keyboard_mode_layout'
        with open(menu_data_path) as file:
            keyboard_mode_data = json.loads(file.read())
            keyboard_mode = keyboard_mode_data['key']
        for mode in keyboard_mode:
            if mode == which_one:
                self.driver.tap([(str(float(mode['x']) * float(screen_size_width)),
                                  str(float(mode['x']) * float(screen_size_height)))])

    # 编辑键盘
    def adjust_size(self):
        pass

    # 剪切板
    def clipboard_func(self):
        pass

    # 编辑
    def edit(self):
        pass

    # 声音和振动
    def sound_vibration(self):
        pass





