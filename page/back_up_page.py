import time

from commons.base_function import BaseFunction


class BackUpPage(BaseFunction):
    # 自动同步设置项CheckBox
    def automatically_sync_settings(self, to_do):
        """
        :param to_do: 勾选为true，不勾选为false
        :return:
        """
        check_status = self.find_element_by_xpath('//*[@text="键盘布局"]/following-sibling::android.widget.CheckBox').\
            get_attribute('checked')
        if check_status == to_do:
            print('勾选状态为：', check_status)
        else:
            self.find_element_by_xpath_click('//*[@text="键盘布局"]/following-sibling::android.widget.CheckBox')

    # 备份设置项
    def backup_setting(self, to_do):
        """
        :param to_do: 取消/确定
        :return:
        """
        self.find_element_by_xpath_click('//*[@text="备份设置项"]')
        time.sleep(1)
        self.find_element_by_xpath_click('//*[@text="%s"]' % to_do)

    # 恢复设置项
    def restore_setting(self, to_do):
        """
        :param to_do: 取消/确定
        :return:
        """
        self.find_element_by_xpath_click('//*[@text="恢复设置项"]')
        time.sleep(1)
        self.find_element_by_xpath_click('//*[@text="%s"]' % to_do)
        self.driver.implicitly_wait(10)
        # self.find_element_by_xpath_click('//*[@text="%s"]' % '完成')
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/backup_dialog_button').click()

    # 清空云备份
    def clear_backup(self, to_do):
        """
        :param to_do: 取消/确定
        :return:
        """
        self.find_element_by_xpath_click('//*[@text="清空云备份"]')
        time.sleep(1)
        self.find_element_by_xpath_click('//*[@text="%s"]' % to_do)

