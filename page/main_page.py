from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction
from .gdpr_page import GdprPage


# 设置默认输入法的页面
class MainPage(BaseFunction):
    # 选择小艺输入法页面，'在设置中启用'控件
    _enable_input_method = (By.ID, 'com.huawei.ohos.inputmethod:id/enable_input_method')
    # '选择输入法'控件
    _xpath_locator_switch = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                             'android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/'
                             'android.widget.LinearLayout/android.widget.FrameLayout[2]/'
                             'android.widget.LinearLayout/android.widget.LinearLayout/'
                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                             'androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/'
                             'android.widget.LinearLayout/android.widget.Switch')
    _id_locator_input_method = (By.ID, 'com.huawei.ohos.inputmethod:id/select_input_method')
    _xpath_locator_ohos = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.ListView/'
                                     'android.widget.LinearLayout[3]')

    def set_default_method(self):
        # if len(self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/cb_join')) > 1:
        #     return GdprPage(self.driver)
        if self.elements_judge(self._enable_input_method):
            self.find_element_click(self._enable_input_method)
        if self.elements_judge(self._xpath_locator_switch):
            self.find_element_click(self._xpath_locator_switch)
            # self.driver.find_element_by_xpath('//*[text()="小艺输入法"]/../../android.widget.LinearLayout/android.widget.Switch')
            self.driver.switch_to_alert().accept()
            # self.find_element_by_text_click("确定")
        if self.elements_judge(self._id_locator_input_method):
            self.find_element_click(self._id_locator_input_method)
            self.find_element_by_text_click("小艺输入法")

        return GdprPage(self.driver)
