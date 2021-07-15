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
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def xpath_vib_drag_bar(self):
        self.find_element_click(self._xpath_vib_drag_bar)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def xpath_sound_drag_bar(self):
        self.find_element_click(self._xpath_sound_drag_bar)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def to_sound_effect_page(self):
        self.find_element_click(self._xpath_sound_effect)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)




