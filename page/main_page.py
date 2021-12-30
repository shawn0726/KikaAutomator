from selenium.webdriver.common.by import By


from page.gdpr_page import GdprPage
from public.base_function import BaseFunction


class MainPage(BaseFunction):
    def set_default_method(self):
        # if len(self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/cb_join')) > 1:
        #     return GdprPage(self.driver)
        #
        main_page = MainPage(self.driver)
        # 设置默认输入法第一步：'在设置中启用'，首先判断按键是否点击，若不能点击则直接点击'2.选择输入法'
        if main_page.is_element_exist('在设置中启用'):
            if main_page.find_element_by_text('在设置中启用').is_enabled():
                main_page.find_element_by_text_click('在设置中启用')
                # 进入'语言和输入法'设置页面，通过滑动的方式，寻找并选择'小艺输入法'
                main_page.move_to_find_text('小艺输入法')
                # 通过'小艺输入法'text定位同级元素，即右侧的滑块
                self.driver.find_element_by_xpath('//*[@text="小艺输入法"]/../following-sibling::android.widget'
                                                  '.LinearLayout//*[@resource-id="android:id/switch_widget"]').click()
                # 点击注意弹框中的'确定'按钮
                main_page.find_element_by_text_click('确定')
                self.driver.implicitly_wait(5)
            #     首先判断'2.选择输入法'是否可以点击
            if main_page.find_element_by_text('选择输入法').is_enabled():
                main_page.find_element_by_text_click('选择输入法')
                main_page.find_element_by_text_click('小艺输入法')
                return GdprPage(self.driver)
        return GdprPage(self.driver)
