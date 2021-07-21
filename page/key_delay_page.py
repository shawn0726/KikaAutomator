from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class KeyDelayPage(BaseFunction):
    _progress_bar_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                       'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                       'android.widget.FrameLayout/android.widget.FrameLayout/'
                                                       'androidx.appcompat.widget.LinearLayoutCompat/'
                                                       'android.widget.FrameLayout/android.widget.FrameLayout/'
                                                       'android.widget.LinearLayout/android.widget.SeekBar')
    _default_capitalization_checkbox = (By.ID, 'android:id/button3')
    _cancel_capitalization_checkbox = (By.ID, 'android:id/button2')
    _determine_capitalization_checkbox = (By.ID, 'android:id/button1')

    def adjust_progress_capitalization(self, size):
        screen_size_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_size_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        #print(screen_size_width)
        #print(screen_size_height)
        if size == 'max':
            self.touch_tap(x=0.846 * float(screen_size_width), y=0.58 * float(screen_size_height))
        if size == 'min':
            self.touch_tap(x=0.16 * float(screen_size_width), y=0.58 * float(screen_size_height))
        if size == 'middle':
            self.touch_tap(x=0.39 * float(screen_size_width), y=0.58 * float(screen_size_height))
            return KeyDelayPage(self.driver)

    def check_default_capitalization(self):
        self.find_element_click(self._default_capitalization_checkbox)
        from page.page_setting_page import PageSettingPage
        return PageSettingPage(self.driver)

    def check_cancel_capitalization(self):
        self.find_element_click(self._cancel_capitalization_checkbox)
        from page.page_setting_page import PageSettingPage
        return PageSettingPage(self.driver)

    def check_determine_capitalization(self):
        self.find_element_click(self._determine_capitalization_checkbox)
        from page.page_setting_page import PageSettingPage
        return PageSettingPage(self.driver)