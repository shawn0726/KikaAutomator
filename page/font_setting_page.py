from public.base_function import BaseFunction
from selenium.webdriver.common.by import By


class FontSettingPage(BaseFunction):
    _xpath_locator_font_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_font1_pre_select = ('//android.widget.FrameLayout[@content-desc="Default 字体，双击即可选择使用"]'
                               '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font1_now_select = ('//android.widget.FrameLayout[@content-desc="Default 字体，正在使用"]/'
                               'android.widget.FrameLayout[2]/android.widget.ImageView[1]')
    _xpath_font2_pre_select = ('//android.widget.FrameLayout[@content-desc="MidoRound 字体，双击即可选择使用"]'
                               '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font2_now_select = ('//android.widget.FrameLayout[@content-desc="Default 字体，正在使用"]/'
                               'android.widget.FrameLayout[2]/android.widget.ImageView[1]')
    _xpath_font3_pre_select = ('//android.widget.FrameLayout[@content-desc="Joker 字体，双击即可选择使用"]'
                               '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font3_now_select = ('//android.widget.FrameLayout[@content-desc="Default 字体，正在使用"]/'
                               'android.widget.FrameLayout[2]/android.widget.ImageView[1]')
    _xpath_font4_pre_select = ('//android.widget.FrameLayout[@content-desc="AriaSlab 字体，双击即可选择使用"]'
                               '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font4_now_select = ('//android.widget.FrameLayout[@content-desc="AriaSlab 字体，正在使用"]/'
                               'android.widget.FrameLayout[2]/android.widget.ImageView[1]')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_font_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def switch_font1(self):
        if self.driver.find_elements_by_xpath(self._xpath_font1_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font1_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font1_now_select).click()
        self.screenshot()
        # 比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/font1.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return FontSettingPage(self.driver)

    def switch_font2(self):
        if self.driver.find_elements_by_xpath(self._xpath_font2_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font2_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font2_now_select).click()
        self.screenshot()
        # 比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/font2.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return FontSettingPage(self.driver)

    def switch_font3(self):
        if self.driver.find_elements_by_xpath(self._xpath_font3_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font3_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font3_now_select).click()
        self.screenshot()
        # 比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/font3.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return FontSettingPage(self.driver)

    def switch_font4(self):
        if self.driver.find_elements_by_xpath(self._xpath_font4_pre_select):
            print("不为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font4_pre_select).click()
        else:
            print("为当前主题")
            self.driver.find_element_by_xpath(self._xpath_font4_now_select).click()
        self.screenshot()
        # 比较截图是否一致
        self.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/font4.png',
                     r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp.png')
        self.find_element_by_text_click('快来试试吧。')
        return FontSettingPage(self.driver)
