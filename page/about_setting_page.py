import os

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class AboutSettingPage(BaseFunction):
    _xpath_locator_about_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_disable_service = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                        'android.widget.FrameLayout/android.widget.LinearLayout/'
                                        'android.widget.FrameLayout/android.view.ViewGroup/'
                                        'android.view.ViewGroup/android.widget.TextView[2]')
    _xpath_privacy_page = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup')
    _xpath_user_agreement = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                       'android.widget.FrameLayout/android.widget.LinearLayout/'
                                       'android.widget.FrameLayout/android.view.ViewGroup/'
                                       'android.view.ViewGroup/android.widget.TextView[1]')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_about_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def to_disable_service(self):
        self.find_element_click(self._xpath_disable_service)
        from page.disable_service_page import DisableServicePage
        return DisableServicePage(self.driver)

    def check_xpath_privacy_page(self):
        self.find_element_click(self._xpath_privacy_page)
        os.system('adb shell input keyevent 4')
        return AboutSettingPage(self.driver)

    def check_xpath_user_agreement(self):
        self.find_element_click(self._xpath_user_agreement)
        os.system('adb shell input keyevent 4')
        return AboutSettingPage(self.driver)
