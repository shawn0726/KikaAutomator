import os
import time

from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction



class GdprPage(BaseFunction):
    _gdpr_join_checkbox = (By.ID, 'com.huawei.ohos.inputmethod:id/cb_join')
    _gdpr_agree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_right')
    _gdpr_disagree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_left')
    _gdpr_learn_more_button = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_content2')

    def agree_gdpr(self):
        if self.elements_judge(self._gdpr_join_checkbox):
            self.find_element_click(self._gdpr_join_checkbox)
            self.find_element_click(self._gdpr_agree_button)
        else:
            self.find_element_click(self._gdpr_agree_button)
            time.sleep(2)
            self.find_element_click(self._gdpr_agree_button)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def disagree_gdpr(self):
        self.find_element_click(self._gdpr_disagree_button)
        return
