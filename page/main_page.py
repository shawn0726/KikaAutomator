from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction
from .gdpr_page import GdprPage


# 设置默认输入法的页面
class MainPage(BaseFunction):
    '''
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
    '''
    def set_default_method(self):
        # if len(self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/cb_join')) > 1:
        #     return GdprPage(self.driver)
        #
        main_page = MainPage(self.driver)
        # 设置默认输入法第一步：'在设置中启用'，首先判断按键是否点击，若不能点击则直接点击'2.选择输入法'
        if main_page.is_element_exist('1.在设置中启用'):
            if main_page.find_element_by_text('1.在设置中启用').is_enabled():
                main_page.find_element_by_text_click('1.在设置中启用')
                # 进入'语言和输入法'设置页面，通过滑动的方式，寻找并选择'小艺输入法'
                # self.driver.find_element_by_android_uiautomator(
                #     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                #     '.text("小艺输入法").instance(0));')
                main_page.move_to_find_text('小艺输入法')
                # 通过'小艺输入法'text定位同级元素，即右侧的滑块
                self.driver.find_element_by_xpath('//*[@text="小艺输入法"]/../following-sibling::android.widget'
                                                  '.LinearLayout//*[@resource-id="android:id/switch_widget"]').click()
                # 点击注意弹框中的'确定'按钮
                main_page.find_element_by_text_click('确定')
                self.driver.implicitly_wait(5)
            #     首先判断'2.选择输入法'是否可以点击
            if main_page.find_element_by_text('2.选择输入法').is_enabled():
                main_page.find_element_by_text_click('2.选择输入法')
                main_page.find_element_by_text_click('小艺输入法')

        '''
        if self.is_element_exist(self._enable_input_method):
            self.find_element_click(self._enable_input_method)
        if self.is_element_exist(self._xpath_locator_switch):
            self.find_element_click(self._xpath_locator_switch)
            # self.driver.find_element_by_xpath('//*[text()="小艺输入法"]/../../android.widget.LinearLayout/android.widget.Switch')
            self.driver.switch_to_alert().accept()
            # self.find_element_by_text_click("确定")
        if self.is_element_exist(self._id_locator_input_method):
            self.find_element_click(self._id_locator_input_method)
            self.find_element_by_text_click("小艺输入法")
        '''
        return GdprPage(self.driver)
