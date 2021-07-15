from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class PageSettingPage(BaseFunction):
    _xpath_locator_page_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _bubble_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                 'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                 'android.widget.FrameLayout/android.view.ViewGroup/'
                                                 'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                 'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                 'androidx.recyclerview.widget.RecyclerView/'
                                                 'android.widget.LinearLayout[1]/android.widget.RelativeLayout')
    _number_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                 'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                 'android.widget.FrameLayout/android.view.ViewGroup/'
                                                 'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                 'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                 'androidx.recyclerview.widget.RecyclerView/'
                                                 'android.widget.LinearLayout[2]/android.widget.RelativeLayout')
    _slide_capitalization_checkbox = (By.XPATH,  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                 'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                 'android.widget.FrameLayout/android.view.ViewGroup/'
                                                 'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                 'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                 'androidx.recyclerview.widget.RecyclerView/'
                                                 'android.widget.LinearLayout[4]/android.widget.RelativeLayout')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_page_setting_back)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_bubble_capitalization(self, status):
        if status:
            if not (self.find_element(self._bubble_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('按键气泡')
        else:
            if self.find_element(self._bubble_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('按键气泡')

    def check_number_capitalization(self, status):
        if status:
            if not (self.find_element(self._number_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('数字行')
        else:
            if self.find_element(self._number_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('数字行')

    def check_slide_capitalization(self, status):
        if status:
            if not (self.find_element(self._slide_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('滑动指示效果')
        else:
            if self.find_element(self._slide_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('滑动指示效果')