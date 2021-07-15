from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class ThemeSettingPage(BaseFunction):
    _xpath_locator_theme_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_them1_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="TestPos 主题"]/'
                                     'android.widget.ImageView')
    _xpath_them2_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Wind 主题"]/'
                                     'android.widget.FrameLayout')
    _xpath_them3_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Material Dark 主题"]/'
                                     'android.widget.ImageView')
    _xpath_them4_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Concise 主题"]/'
                                     'android.widget.ImageView')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_theme_setting_back)

    def switch_them1(self):
        self.find_element(self._xpath_them1_select)

    def switch_them2(self):
        self.find_element(self._xpath_them2_select)

    def switch_them3(self):
        self.find_element(self._xpath_them3_select)

    def switch_them4(self):
        self.find_element(self._xpath_them4_select)
