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
                                                   'android.widget.LinearLayout/android.widget.Switch'). \
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

    # 候选词字体大小
    def candidate_size(self, multiple):
        """

        :param multiple: multiple (0,1)
        :return:
        """
        status = self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]/../following-sibling::'
                                                   'android.widget.LinearLayout/android.widget.Switch'). \
            get_attribute('checked')
        self.driver.implicitly_wait(15)
        if status == 'true':
            self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]').click()
        seekbar_bounds = self.container_bounds('font_size_seekbar', 'resource_id')
        seekbar_bounds_length = seekbar_bounds[2] - seekbar_bounds[0]
        seekbar_bounds_y = (seekbar_bounds[1] + seekbar_bounds[3]) / 2
        self.touch_tap(seekbar_bounds_length * multiple, seekbar_bounds_y)

    # 恢复默认设置
    def font_size_restore_default(self):
        if self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]/../following-sibling::'
                                             'android.widget.LinearLayout/android.widget.Switch'). \
                get_attribute('checked') == 'true':
            self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]').click()
        self.driver.implicitly_wait(15)
        self.find_element_by_id('com.huawei.ohos.inputmethod:id/restore_default_candidate_font_size_checkbox'). \
            click()

    # 键盘字体大小
    def keyboard_font_size(self, multiple):
        if self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]/../following-sibling::'
                                             'android.widget.LinearLayout/android.widget.Switch'). \
                get_attribute('checked') == 'true':
            self.driver.find_element_by_xpath('//*[@text="跟随系统设置调节字体大小"]').click()
        seekbar_bounds = self.container_bounds('keyboard_font_size_seekbar', 'resource_id')
        seekbar_bounds_length = seekbar_bounds[2] - seekbar_bounds[0]
        seekbar_bounds_y = (seekbar_bounds[1] + seekbar_bounds[3]) / 2
        self.touch_tap(seekbar_bounds_length * multiple, seekbar_bounds_y)
