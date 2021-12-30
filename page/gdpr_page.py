import os
import time

from selenium.webdriver.common.by import By

from public.base_function import BaseFunction


class GdprPage(BaseFunction):
    _gdpr_confirm_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_confirm')
    _gdpr_full_experience = (By.ID, 'com.huawei.ohos.inputmethod:id/ll_full_experience')
    _gdpr_base_typing = (By.ID, 'com.huawei.ohos.inputmethod:id/ll_base_typing')

    def full_experience_gdpr(self):
        # 页面存在'Celia Keyboard'证明进入gdpr页面
        if self.is_element_exist('小艺输入法'):
            print("aaaa")
            self.find_element_click(self._gdpr_full_experience)
            self.find_element_click(self._gdpr_confirm_button)

    def base_typing_gdpr(self):
        self.find_element_click(self._gdpr_base_typing)
        self.find_element_click(self._gdpr_confirm_button)

