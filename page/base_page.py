from public.base_function import BaseFunction


class BasePage(BaseFunction):
    def click_syspage_app_management(self):
        self.find_element_by_text_click('应用管理')

    def click_syspage_app_info(self):
        self.find_element_by_text_click('权限')

    def click_syspage_universal(self, text):
        self.find_element_by_text_click(text)

    def click_syspage_agree_button(self):
        self.find_element_by_text_click('始终允许')
