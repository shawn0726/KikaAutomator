import sys

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By
# import sys
# sys.setrecursionlimit(100000)


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
    _delay_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                'android.widget.FrameLayout/android.view.ViewGroup/'
                                                'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                'androidx.recyclerview.widget.RecyclerView/'
                                                'android.widget.LinearLayout[3]/android.widget.RelativeLayout/'
                                                'android.widget.TextView[1]')
    _slide_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                'android.widget.FrameLayout/android.view.ViewGroup/'
                                                'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                'androidx.recyclerview.widget.RecyclerView/'
                                                'android.widget.LinearLayout[4]/android.widget.RelativeLayout/'
                                                'android.widget.TextView[1]')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_page_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_bubble_capitalization(self):
        self.find_element_click(self._bubble_capitalization_checkbox)
        return PageSettingPage(self.driver)

    def check_number_capitalization(self):
        self.find_element_click(self._number_capitalization_checkbox)
        return PageSettingPage(self.driver)

    def to_delay_page(self):
        self.find_element_click(self._delay_capitalization_checkbox)
        #self.find_element_click(self._progress_bar_capitalization_checkbox)
        #self.swipLeft(self.driver, t=1000, n=600)
        from page.key_delay_page import KeyDelayPage
        return KeyDelayPage(self.driver)

    def check_slide_capitalization(self):
        self.find_element_click(self._slide_capitalization_checkbox)
        return PageSettingPage(self.driver)