import time

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class ThemeSettingPage(BaseFunction):
    _xpath_locator_theme_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_them1_pre_select = ('//android.widget.FrameLayout[@content-desc="TestPos 主题"]/'
                               'android.widget.ImageView')
    _xpath_them1_now_select = ('//android.widget.FrameLayout[@content-desc="TestPos 主题，正在使用"]/'
                               'android.widget.FrameLayout')
    _xpath_them2_pre_select = ('//android.widget.FrameLayout[@content-desc="Wind 主题"]/'
                               'android.widget.ImageView')
    _xpath_them2_now_select = ('//android.widget.FrameLayout[@content-desc="Wind 主题，正在使用"]/'
                               'android.widget.FrameLayout')
    _xpath_them3_pre_select = ('//android.widget.FrameLayout[@content-desc="Material Dark 主题"]/'
                               'android.widget.ImageView')
    _xpath_them3_now_select = ('//android.widget.FrameLayout[@content-desc="Material Dark 主题，正在使用"]/'
                               'android.widget.FrameLayout')
    _xpath_them4_pre_select = ('//android.widget.FrameLayout[@content-desc="Concise 主题"]/'
                               'android.widget.ImageView')
    _xpath_them4_now_select = ('//android.widget.FrameLayout[@content-desc="Concise 主题，正在使用"]/'
                               'android.widget.FrameLayout')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_theme_setting_back)
        time.sleep(2)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def switch_them1(self):
        if self.driver.find_elements_by_xpath(self._xpath_them1_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them1_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them1_now_select).click()
        self.screenshot()
        #比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/theme1.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return ThemeSettingPage(self.driver)

    def switch_them2(self):
        if self.driver.find_elements_by_xpath(self._xpath_them2_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them2_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them2_now_select).click()
        self.screenshot()
        #比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/theme2.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return ThemeSettingPage(self.driver)


    def switch_them3(self):
        if self.driver.find_elements_by_xpath(self._xpath_them3_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them3_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them3_now_select).click()
        self.screenshot()
        #比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/theme3.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return ThemeSettingPage(self.driver)

    def switch_them4(self):
        if self.driver.find_elements_by_xpath(self._xpath_them4_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them4_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_them4_now_select).click()
        self.screenshot()
        #比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/theme4.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return ThemeSettingPage(self.driver)
