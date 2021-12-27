import time

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class FontsizePage(BaseFunction):
    _xpath_locator_input_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_input_setting_back)
        from page.page_setting_page import PageSettingPage
        return PageSettingPage(self.driver)

    # 获取'跟随系统设置调节字体大小'开关状态
    def get_follow_system_setting_status(self):
        status = self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]/../following-sibling::'
                                                   'android.widget.LinearLayout/android.widget.Switch').\
            get_attribute('checked')
        return status

    # 点击'输入设置'页面的设置项
    def follow_system_settings(self, to_do):
        status = self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]/../following-sibling::'
                                                   'android.widget.LinearLayout/android.widget.Switch'). \
            get_attribute('checked')
        self.driver.implicitly_wait(15)
        if to_do == status:
            print('当前状态一致')
        else:
            self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]').click()

    def candidate_size(self):
        status = self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]/../following-sibling::'
                                                   'android.widget.LinearLayout/android.widget.Switch'). \
            get_attribute('checked')
        self.driver.implicitly_wait(15)
        if status == 'true':
            self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]').click()
