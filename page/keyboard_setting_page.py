from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction
from page.input_page import InputPage


#app主页页面
from page.language_setting_page import LanguageSettingPage
from page.theme_setting_page import ThemeSettingPage
from page.font_setting_page import FontSettingPage
from page.page_setting_page import PageSettingPage
from page.input_setting_page2 import InputSettingPage
from page.voice_setting_page import VoiceSettingPage
from page.about_setting_page import AboutSettingPage


class KeyboardSettingPage(BaseFunction):
    _xpath_locator_setting_back = (By.XPATH,
                                   '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    # //android.widget.ImageButton[@content-desc="转到上一层级"]

    def back_to_input_page(self):
        self.find_element_click(self._xpath_locator_setting_back)
        return InputPage(self.driver)
        # os.system('adb shell am start -S com.xinmei365.emptyinput/.MainActivity')
        # os.system('adb shell input tap 500 500')

    def to_language_setting_page(self):
        self.find_element_by_text_click('语言')
        return LanguageSettingPage(self.driver)

    def to_theme_setting_page(self):
        self.find_element_by_text_click('主题')
        return ThemeSettingPage(self.driver)

    def to_font_setting_page(self):
        self.find_element_by_text_click('字体')
        return FontSettingPage(self.driver)

    def to_page_setting_page(self):
        self.find_element_by_text_click('页面设置')
        return PageSettingPage(self.driver)

    def to_input_setting_page(self):
        self.find_element_by_text_click('输入设置')
        return InputSettingPage(self.driver)

    def to_voice_setting_page(self):
        self.find_element_by_text_click('音效和振动')
        return VoiceSettingPage(self.driver)

    def to_about_setting_page(self):
        self.find_element_by_text_click('关于')
        return AboutSettingPage(self.driver)





