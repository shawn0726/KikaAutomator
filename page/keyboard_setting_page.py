from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction
from page.input_page import InputPage
from page.input_setting_page import InputSettingPage


class KeyboardSettingPage(BaseFunction):
    _xpath_locator_setting_back = (By.XPATH,
                                   '//android.widget.ImageButton[@content-desc="转到上一层级"]')

    def back_to_input_page(self):
        self.find_element_click(self._xpath_locator_setting_back)
        return InputPage(self.driver)
        # os.system('adb shell am start -S com.xinmei365.emptyinput/.MainActivity')
        # os.system('adb shell input tap 500 500')

    def to_input_setting_page(self):
        self.find_element_by_text_click('输入设置')
        return InputSettingPage(self.driver)
