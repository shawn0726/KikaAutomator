from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class VoiceSettingPage(BaseFunction):
    _xpath_locator_voice_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_vib_drag_bar = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.view.ViewGroup/'
                                     'android.widget.ScrollView/android.widget.RelativeLayout/'
                                     'android.widget.SeekBar[1]')
    _xpath_sound_drag_bar = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                       'android.widget.FrameLayout/android.widget.LinearLayout/'
                                       'android.widget.FrameLayout/android.view.ViewGroup/'
                                       'android.widget.ScrollView/android.widget.RelativeLayout/'
                                       'android.widget.SeekBar[2]')
    _xpath_sound_effect = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/'
                                     'android.widget.RelativeLayout/android.widget.LinearLayout/'
                                     'android.widget.TextView')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_voice_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def adjust_vib_drag_bar(self, size):
        self.find_element_click(self._xpath_vib_drag_bar)
        screen_size_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_size_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        # print(screen_size_width)
        # print(screen_size_height)
        # 1080 2340
        #[12,431][1068,575]
        #97 506
        if size == 'max':
            self.touch_tap(x=0.98 * float(screen_size_width), y=0.24 * float(screen_size_height))
        if size == 'min':
            self.touch_tap(x=0.06 * float(screen_size_width), y=0.24 * float(screen_size_height))
        if size == 'middle':
            self.touch_tap(x=0.45 * float(screen_size_width), y=0.24 * float(screen_size_height))
        return VoiceSettingPage(self.driver)

    def adjust_sound_drag_bar(self, size):
        self.find_element_click(self._xpath_sound_drag_bar)
        screen_size_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_size_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        print(screen_size_width)
        print(screen_size_height)
        if size == 'max':
            self.touch_tap(x=0.96 * float(screen_size_width), y=0.38 * float(screen_size_height))
        if size == 'min':
            self.touch_tap(x=0.06 * float(screen_size_width), y=0.35 * float(screen_size_height))
        if size == 'middle':
            self.touch_tap(x=0.45 * float(screen_size_width), y=0.35 * float(screen_size_height))
        return VoiceSettingPage(self.driver)

    def to_sound_effect_page(self):
        self.find_element_click(self._xpath_sound_effect)
        from page.keyboard_setting_page import KeyboardSettingPage
        return VoiceSettingPage(self.driver)




