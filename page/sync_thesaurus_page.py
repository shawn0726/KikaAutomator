import time

from page.base_page import BasePage

"""
    同步词库页面
"""


class SyncThesaurusPage(BasePage):
    # 同步词库
    def sync_thesaurus(self):
        # self.find_element_by_text_click('//*[@text="同步词库"]')
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/thesaurus_sync').click()

    # 自动同步
    def auto_sync_thesaurus(self):
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/thesaurus_auto_checkbox').click()

    # 删除词库
    def delete_thesaurus(self, to_do):
        """

        :param to_do: 取消、确定
        :return:
        """
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/thesaurus_clear').click()
        time.sleep(1)
        self.find_element_by_text_click('//*[@text="%s"]' % to_do)

    # 获取同步时间
    def get_sync_time(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/thesaurus_complete_arrow')
        str_text = self.find_element_by_id('com.huawei.ohos.inputmethod:id/thesaurus_last_sync_time').get_attribute('text')
        str_time = str_text.replace('上次同步时间：', '')
        return str_time
