import os

from public.base_function import BaseFunction
from selenium.webdriver.common.by import By


class AboutSettingPage(BaseFunction):
    _xpath_locator_about_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')

    # 返回设置页面
    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_about_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    # 停止服务
    def to_disable_service(self):
        self.driver.find_element_by_xpath('//*[@text="%s"]' % '停止服务').click()
        from page.disable_service_page import DisableServicePage
        return DisableServicePage(self.driver)

    """
        开放源代码许可、小艺输入法用户协议和关于小艺输入法与隐私的声明，三者合并为一个 text ，这种情况如何点击？除了坐标是否还有其他方法？
    """