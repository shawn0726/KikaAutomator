import sys

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By
# import sys
# sys.setrecursionlimit(100000)


class PageSettingPage(BaseFunction):
    _xpath_locator_page_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _bubble_capitalization_checkbox = (By.XPATH, '')
    _number_capitalization_checkbox = (By.XPATH, '')
    _slide_capitalization_checkbox = (By.XPATH, '')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_page_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_bubble_capitalization(self):
        self.find_element_click(self._bubble_capitalization_checkbox)
        return PageSettingPage(self.driver)

    def check_number_capitalization(self):
        self.find_element_click(self._number_capitalization_checkbox)
        return PageSettingPage(self.driver)

    def check_slide_capitalization(self, status):
        if status:
            if not (self.find_element(self._slide_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('滑动指示效果')
        else:
            if self.find_element(self._slide_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('滑动指示效果')