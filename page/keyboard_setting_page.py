from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction
from page.input_page import InputPage


#app主页页面
from page.language_setting_page import LanguageSettingPage
from page.theme_setting_page import ThemeSettingPage
from page.font_setting_page2 import FontSettingPage2
from page.page_setting_page import PageSettingPage
from page.input_setting_page2 import InputSettingPage
from page.sound_and_vibration_page import SoundAndVibrationPage
from page.about_setting_page import AboutSettingPage
from page.thesaurus_setting_page import ThesaurusSettingPage
from page.voice_setting_page import VoiceSettingPage


class KeyboardSettingPage(BaseFunction):
    _xpath_locator_setting_back = (By.XPATH,
                                   '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    # //android.widget.ImageButton[@content-desc="转到上一层级"]

    # 返回输入页面
    def back_to_input_page(self):
        self.find_element_click(self._xpath_locator_setting_back)
        return InputPage(self.driver)
        # os.system('adb shell am start -S com.xinmei365.emptyinput/.MainActivity')
        # os.system('adb shell input tap 500 500')

    # 进入语言选择页面
    def to_language_setting_page(self):
        self.find_element_by_text_click('语言')
        return LanguageSettingPage(self.driver)

    # 进入皮肤设置页面
    def to_theme_setting_page(self):
        self.find_element_by_text_click('皮肤')
        return ThemeSettingPage(self.driver)

    # 进入字体设置页面
    def to_font_setting_page(self):
        self.find_element_by_text_click('字体')
        return FontSettingPage2(self.driver)

    # 进入页面设置页面
    def to_page_setting_page(self):
        self.find_element_by_text_click('页面设置')
        return PageSettingPage(self.driver)

    # 进入输入设置页面
    def to_input_setting_page(self):
        self.find_element_by_text_click('输入设置')
        return InputSettingPage(self.driver)

    # 进入语音设置页面
    def to_voice_setting_page(self):
        self.find_element_by_text_click('语音设置')
        return VoiceSettingPage(self.driver)

    # 进入手写设置页面
    def to_write_setting_page(self):
        self.find_element_by_text_click('手写设置')
        return InputSettingPage(self.driver)

    # 进入音效和振动页面
    def to_sound_and_vibration_page(self):
        self.find_element_by_text_click('音效和振动')
        return SoundAndVibrationPage(self.driver)

    # 进入词库设置页面
    def to_thesaurus_setting_page(self):
        self.find_element_by_text_click('词库设置')
        return ThesaurusSettingPage(self.driver)

    # 恢复默认设置
    def restore_to_default_settings(self, to_do):
        self.find_element_by_text_click('恢复默认设置')
        self.driver.implicitly_wait(15)
        self.find_element_by_xpath('//*[@text="%s"]' % to_do).click()

    # 关于
    def to_about_setting_page(self):
        self.find_element_by_text_click('关于')
        return AboutSettingPage(self.driver)





