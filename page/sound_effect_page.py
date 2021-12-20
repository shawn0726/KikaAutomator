from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class SoundEffectPage(BaseFunction):
    _xpath_locator_soundEffect_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _xpath_sound1_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Default 按键音效，正在使用"]/'
                                      'android.widget.FrameLayout[2]/android.widget.ImageView[1]')
    _xpath_sound2_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Typewriter 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound3_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Gun 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound4_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Cup 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound5_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Silencing Shot 按键音效，双击可选择使用"]'
                                      '/android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound6_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Tune 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound7_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Ring1 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound8_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Rubber Duck 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_sound9_select = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Ring2 按键音效，双击可选择使用"]/'
                                      'android.widget.FrameLayout/android.widget.ImageView')
    _xpath_success_select=(By.ID, 'com.huawei.ohos.inputmethod:id/tv_desc')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_soundEffect_setting_back)
        from page.sound_and_vibration_page import SoundAndVibrationPage
        return SoundAndVibrationPage(self.driver)

    def switch_sound1(self):
        self.find_element_click(self._xpath_sound1_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound2(self):
        self.find_element_click(self._xpath_sound2_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound3(self):
        self.find_element_click(self._xpath_sound3_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound4(self):
        self.find_element_click(self._xpath_sound4_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound5(self):
        self.find_element_click(self._xpath_sound5_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound6(self):
        self.find_element_click(self._xpath_sound6_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound7(self):
        self.find_element_click(self._xpath_sound7_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound8(self):
        self.find_element_click(self._xpath_sound8_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)

    def switch_sound9(self):
        self.find_element_click(self._xpath_sound9_select)
        self.find_element_click(self._xpath_success_select)
        return SoundEffectPage(self.driver)
