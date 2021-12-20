import time

from commons.base_function import BaseFunction


class LoginPage(BaseFunction):
    # 登录
    def log_in(self, to_do):
        """
        :param to_do: 是否从云端恢复设置项数据：取消、确定
        :return:
        """
        self.find_element_by_xpath_click('//*[@resource-id="com.huawei.ohos.inputmethod:id/account_icon_login"]')
        self.driver.implicitly_wait(15)
        self.find_element_by_xpath_click('//*[@text="%s"]' % to_do)

    # 退出
    def log_out(self, to_do):
        """
        :param to_do:  请再次确认是否退出：取消、继续退出
        :return:
        """
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/account_exit_login').click()
        self.driver.implicitly_wait(15)
        self.find_element_by_xpath_click('//*[@text="%s"]' % to_do)

    # 我的皮肤
    def my_skins(self):
        self.find_element_by_xpath_click('//*[@text="我的皮肤"]')
        from page.theme_setting_page import ThemeSettingPage
        return ThemeSettingPage(self.driver)

    # 我的字体
    def my_fonts(self):
        self.find_element_by_xpath_click('//*[@text="我的字体"]')
        from page.font_setting_page2 import FontSettingPage2
        return FontSettingPage2(self.driver)

    # 同步词库
    def my_sync(self):
        self.find_element_by_xpath_click('//*[@text="同步词库"]')
        from page.sync_thesaurus_page import SyncThesaurusPage
        return SyncThesaurusPage(self.driver)

    # 备份设置项
    def my_back_up(self):
        self.find_element_by_xpath_click('//*[@text="备份设置项"]')
        from page.back_up_page import BackUpPage
        return BackUpPage(self.driver)

    # 设置
    def to_setting_page(self):
        self.find_element_by_xpath_click('//*[@text="设置"]')
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)
