from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class InputSettingPage(BaseFunction):
    _xpath_locator_input_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    _auto_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.view.ViewGroup/'
                                               'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                               'android.widget.LinearLayout/android.widget.FrameLayout/'
                                               'androidx.recyclerview.widget.RecyclerView/'
                                               'android.widget.LinearLayout[3]/android.widget.LinearLayout/'
                                               'android.widget.CheckBox')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_input_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_auto_capitalization(self, status):
        if status:
            if not (self.find_element(self._auto_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('首字母自动大写')
        else:
            if self.find_element(self._auto_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('首字母自动大写')
