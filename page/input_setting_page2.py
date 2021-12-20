import time

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class InputSettingPage(BaseFunction):
    # 点击'输入设置'页面的设置项
    def click_which_item(self, which, extra_setting):
        """
        :param which: 输入设置里面，打算点击的控件的 text 属性
        :param extra_setting: 当点击'模式设置'的时候，需要填入对应的操作：完整的体验模式、基础的打字模式、取消
        :return:
        """

        try:
            self.driver.find_element_by_xpath('//*[@text="%s"]' % which).click()
            if which == "中文设置":
                from page.chinese_setting_page import ChineseSettingPage
                return ChineseSettingPage(self.driver)
        except:
            container_bounds = self.container_bounds('recycler_view', 'resource_id')
            self.driver.swipe((container_bounds[0] + container_bounds[2]) / 2,
                              (container_bounds[3] - 1),
                              (container_bounds[0] + container_bounds[2]) / 2,
                              (container_bounds[1] + container_bounds[3]) / 2)
            self.driver.find_element_by_xpath('//*[@text="%s"]' % which).click()
            if which == "中文设置":
                from page.chinese_setting_page import ChineseSettingPage
                return ChineseSettingPage(self.driver)
        if which == "模式设置":
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_xpath('//*[@text="%s"]' % extra_setting).click()

    # 检查对应设置项的开闭状态
    def check_item_status(self, which):
        """
        :param which: 输入设置里面，打算点击的控件的 text 属性
        :return: 返回控件 checked 属性
        """
        status = self.driver.find_element_by_xpath(
            '//*[@text="%s"]/../following-sibling::android.widget.LinearLayout/android.widget.CheckBox' % which). \
            get_attribute('checked')
        print('status: ', status)
        return status
