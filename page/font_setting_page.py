from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class FontSettingPage(BaseFunction):
    _xpath_locator_font_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_font1_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Default 字体，双击即可选择使用"]'
                                     '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font2_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="MidoRound 字体，双击即可选择使用"]'
                                     '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font3_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Joker 字体，双击即可选择使用"]'
                                     '/android.widget.FrameLayout/android.widget.TextView')
    _xpath_font4_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="AriaSlab 字体，双击即可选择使用"]'
                                     '/android.widget.FrameLayout/android.widget.TextView')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_font_setting_back)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def switch_font1(self):
        self.find_element(self._xpath_font1_select)

    def switch_font2(self):
        self.find_element(self._xpath_font2_select)

    def switch_font3(self):
        self.find_element(self._xpath_font3_select)

    def switch_font4(self):
        self.find_element(self._xpath_font4_select)
