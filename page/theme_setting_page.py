import time

from public.base_function import BaseFunction
from selenium.webdriver.common.by import By


class ThemeSettingPage(BaseFunction):
    _xpath_locator_theme_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_theme_setting_back)
        time.sleep(2)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def back_to_previous_page(self):
        self.driver.back()

    def switch_theme(self, which_one):
        """
        切换皮肤
        :param which_one: 深色、默认、墨绿色、浅艾蓝
        :return:
        """
        self.find_element_by_xpath('//*[@text="%s"]' % which_one).click()
        self.driver.implicitly_wait(15)
        self.find_element_by_xpath('//android.widget.ImageView[@content-desc="隐藏键盘"]').click()

    def search_selected_theme(self):
        """
        寻找选中的皮肤
        :return: 返回选中皮肤的text属性
        """
        content_list = self.driver.find_elements_by_xpath('//*[@resource-id="com.huawei.ohos.inputmethod:id'
                                                          '/recycler_view"]/android.widget.LinearLayout')
        for item in content_list:
            if '正在使用' in item.get_attribute('content-desc'):
                return self.find_element_by_xpath('//android.widget.LinearLayout['
                                                  '@content-desc="%s"]/android.widget.TextView' % item.get_attribute
                                                  ('content-desc')).get_attribute('text')
