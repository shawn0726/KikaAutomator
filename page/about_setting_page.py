from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class AboutSettingPage(BaseFunction):
    _xpath_locator_about_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_disable_service = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                            'android.widget.FrameLayout/android.widget.LinearLayout/'
                                            'android.widget.FrameLayout/android.view.ViewGroup/'
                                            'android.view.ViewGroup/android.widget.TextView[2]')
    _xpath_privacy_page=(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                   'android.widget.FrameLayout/android.widget.LinearLayout/'
                                   'android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup')
    _xpath_user_agreement=(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.view.ViewGroup/'
                                     'android.view.ViewGroup/android.widget.TextView[1]')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_about_setting_back)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def statement_about_page(self):
        self.find_element_click(self._xpath_disable_service)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def xpath_privacy_page(self):
        self.find_element_click(self.xpath_privacy_page)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def xpath_user_agreement(self):
        self.find_element_click(self._xpath_user_agreement)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)