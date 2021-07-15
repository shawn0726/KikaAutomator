from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class LanguageSettingPage(BaseFunction):
    _xpath_locator_language_setting_back = (By.XPATH, '// android.widget.ImageButton[ @ content - desc = "转到上一层级"]')
    _menu_search_box = (By.ID, 'com.huawei.ohos.inputmethod:id/menu_search_view')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_language_setting_back)
        from page.keboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def input_menu_search(self):
        self.find_element(self._menu_search_box).click()

