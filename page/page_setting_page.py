import sys
import time
from xmlrpc.client import boolean, Boolean

import golVar
from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


# import sys
# sys.setrecursionlimit(100000)


class PageSettingPage(BaseFunction):
    _xpath_locator_page_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _delay_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                'android.widget.FrameLayout/android.view.ViewGroup/'
                                                'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                'androidx.recyclerview.widget.RecyclerView/'
                                                'android.widget.LinearLayout[3]/android.widget.RelativeLayout/'
                                                'android.widget.TextView[1]')
    _select_bubble = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                      'android.widget.FrameLayout/android.view.ViewGroup/'
                      'android.widget.RelativeLayout/android.widget.FrameLayout/'
                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                      'androidx.recyclerview.widget.RecyclerView/'
                      'android.widget.LinearLayout[1]/android.widget.LinearLayout/'
                      'android.widget.CheckBox')
    _select_number = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                      'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                      'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                      'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                      'android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.CheckBox')
    _select_slide = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                     'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                     'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                     'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                     'android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.CheckBox')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_page_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    # 按键气泡
    def check_bubble_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath('//*[@text="按键气泡"]/../following-sibling::android.widget'
                                                      '.LinearLayout/android.widget.Switch').get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                self.driver.find_element_by_xpath('//*[@text="按键气泡"]/../following-sibling::android.widget'
                                                  '.LinearLayout/android.widget.Switch').click()
                nowstatus = self.driver.find_element_by_xpath('//*[@text="按键气泡"]/../following-sibling::android.widget'
                                                              '.LinearLayout/android.widget.Switch').get_attribute(
                    'checked')
                print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath('//*[@text="按键气泡"]/../following-sibling::android.widget'
                                                  '.LinearLayout/android.widget.Switch').click()
                nowstatus = self.driver.find_element_by_xpath('//*[@text="按键气泡"]/../following-sibling::android.widget'
                                                              '.LinearLayout/android.widget.Switch').get_attribute(
                    'checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                print('勾选状态为', nowstatus)

    # 数字行
    def check_number_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                      '.LinearLayout/android.widget.Switch').get_attribute('checked')
        print('nowstatus:', nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                              '.LinearLayout/android.widget.Switch').get_attribute(
                    'checked')
                print('勾选状态为', nowstatus)
                golVar.set_value('language_layout', 'relative_layout_en_num')
            if nowstatus == 'false':
                self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                  '.LinearLayout/android.widget.Switch').click()
                nowstatus = self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                              '.LinearLayout/android.widget.Switch').get_attribute(
                    'checked')
                print('勾选状态为', nowstatus)
                golVar.set_value('language_layout', 'relative_layout_en_num')
        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                  '.LinearLayout/android.widget.Switch').click()
                nowstatus = self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                              '.LinearLayout/android.widget.Switch').get_attribute(
                    'checked')
                print('勾选状态为', nowstatus)
                golVar.set_value('language_layout', 'relative_layout_en')
            if nowstatus == 'false':
                # nowstatus = self.driver.find_element_by_xpath(self._select_number).get_attribute('checked')
                nowstatus = self.driver.find_element_by_xpath('//*[@text="数字行"]/../following-sibling::android.widget'
                                                              '.LinearLayout/android.widget.Switch').get_attribute(
                    'checked')
                print('勾选状态为', nowstatus)
                golVar.set_value('language_layout', 'relative_layout_en')

    def to_key_delay_page(self):
        self.find_element_click(self._delay_capitalization_checkbox)
        # self.find_element_click(self._progress_bar_capitalization_checkbox)
        # self.swipLeft(self.driver, t=1000, n=600)
        from page.key_delay_page import KeyDelayPage
        return KeyDelayPage(self.driver)

    # 按键长按延迟弹框操作
    def button_long_press_delay(self, multiple, do_what):
        """
        :param multiple: 取值(0，1),不取边界值
        :param do_what: 默认、取消、确定
        :return:
        """
        self.driver.find_element_by_xpath('//*[@text="按键长按延迟"]').click()
        self.driver.implicitly_wait(15)
        seek_bar_dialog_bar_bounds = self.container_bounds('seek_bar_dialog_bar', 'resource_id')
        seek_bar_dialog_bar_width = seek_bar_dialog_bar_bounds[2] - seek_bar_dialog_bar_bounds[0]
        self.touch_tap((seek_bar_dialog_bar_bounds[0] + seek_bar_dialog_bar_width * multiple),
                       (seek_bar_dialog_bar_bounds[1] + seek_bar_dialog_bar_bounds[3]) / 2)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath('//*[@text="%s"]' % do_what).click()

    # 滑动指示效果
    def check_slide_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._select_slide).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._select_slide).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                self.driver.find_element_by_xpath(self._select_slide).click()
                nowstatus = self.driver.find_element_by_xpath(self._select_slide).get_attribute('checked')
                print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._select_slide).click()
                nowstatus = self.driver.find_element_by_xpath(self._select_slide).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._select_slide).get_attribute('checked')
                print('勾选状态为', nowstatus)

    # 字体大小
    def change_font_size(self):
        self.driver.find_element_by_xpath('//*[@text="字体大小"]').click()
        return