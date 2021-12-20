from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class DisableServicePage(BaseFunction):
    _xpath_cancel = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_disable_left')
    _xpath_disable = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_disable_right')

    def check_xpath_cancel(self):
        self.driver.find_element_by_xpath('//*[@text="%s"]' % '取消').click()

    def check_xpath_disable(self):
        self.driver.find_element_by_xpath('//*[@text="%s"]' % '停止服务').click()
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)
