from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class DisableServicePage(BaseFunction):
    _xpath_cancel = (By.ID, 'com.kika.photon.inputmethod:id/tv_disable_left')
    _xpath_disable = (By.ID, 'com.kika.photon.inputmethod:id/tv_disable_right')

    def check_xpath_cancel(self):
        self.find_element_click(self._xpath_cancel)
        from page.about_setting_page import AboutSettingPage
        return AboutSettingPage(self.driver)

    def check_xpath_disable(self):
        self.find_element_click(self._xpath_ok)
        from page.about_setting_page import AboutSettingPage
        return AboutSettingPage(self.driver)