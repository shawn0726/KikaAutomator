from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class InputSettingPage(BaseFunction):
    _xpath_locator_input_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    _auto_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.view.ViewGroup/'
                                               'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                               'android.widget.LinearLayout/android.widget.FrameLayout/'
                                               'androidx.recyclerview.widget.RecyclerView/'
                                               'android.widget.LinearLayout[3]/android.widget.LinearLayout/'
                                               'android.widget.CheckBox')
    _slide_input_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'androidx.recyclerview.widget.RecyclerView/'
                                                      'android.widget.LinearLayout[1]/android.widget.RelativeLayout')
    _slide_orbit_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'androidx.recyclerview.widget.RecyclerView/'
                                                      'android.widget.LinearLayout[2]/android.widget.RelativeLayout/'
                                                      'android.widget.TextView')
    _suggest_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                  'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                  'android.widget.FrameLayout/android.view.ViewGroup/'
                                                  'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                  'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                  'androidx.recyclerview.widget.RecyclerView/'
                                                  'android.widget.LinearLayout[4]/android.widget.RelativeLayout/'
                                                  'android.widget.TextView[2')
    _automatic_correct_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                            'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                            'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                            'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                            'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                            'android.widget.FrameLayout/'
                                                            'androidx.recyclerview.widget.RecyclerView/'
                                                            'android.widget.LinearLayout[5]/'
                                                            'android.widget.RelativeLayout')
    _emoji_prediction_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                           'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                           'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                           'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                           'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                           'android.widget.FrameLayout/'
                                                           'androidx.recyclerview.widget.RecyclerView/'
                                                           'android.widget.LinearLayout[6]/'
                                                           'android.widget.RelativeLayout/android.widget.TextView')
    _double_click_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                       'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                       'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                       'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                       'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                       'android.widget.FrameLayout/'
                                                       'androidx.recyclerview.widget.RecyclerView/'
                                                       'android.widget.LinearLayout[7]/android.widget.RelativeLayout/'
                                                       'android.widget.TextView[1]')
    _quickly_insert_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                         'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                         'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                         'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                         'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                         'android.widget.FrameLayout/'
                                                         'androidx.recyclerview.widget.RecyclerView/'
                                                         'android.widget.LinearLayout[8]/android.widget.RelativeLayout/'
                                                         'android.widget.TextView[1]')
    _long_press_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                     'android.widget.LinearLayout/'
                                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                     'android.widget.FrameLayout/android.view.ViewGroup/'
                                                     'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                     'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                     'androidx.recyclerview.widget.RecyclerView/'
                                                     'android.widget.LinearLayout[9]/android.widget.RelativeLayout/'
                                                     'android.widget.TextView[1]')
    _experience_plan_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                          'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                          'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                          'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                          'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                          'android.widget.FrameLayout/'
                                                          'androidx.recyclerview.widget.RecyclerView/'
                                                          'android.widget.LinearLayout[8]/'
                                                          'android.widget.RelativeLayout/'
                                                          'android.widget.TextView[1]')





    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_input_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_slide_input_capitalization(self, status):
        if status:
            if not (self.find_element(self._slide_input_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('启动滑行输入')
        else:
            if self.find_element(self._slide_input_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('启动滑行输入')

    def check_slide_orbit_capitalization(self, status):
        if status:
            if not (self.find_element(self._slide_orbit_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('显示滑行轨迹')
        else:
            if self.find_element(self._slide_orbit_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('显示滑行轨迹')

    def check_auto_capitalization(self, status):
        if status:
            if not (self.find_element(self._auto_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('首字母自动大写')
        else:
            if self.find_element(self._auto_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('首字母自动大写')

    def check_suggest_capitalization(self, status):
        if status:
            if not (self.find_element(self._suggest_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('后续字词建议')
        else:
            if self.find_element(self._suggest_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('后续字词建议')

    def check_automatic_correct_capitalization(self, status):
        if status:
            if not (self.find_element(self._automatic_correct_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('自动校正')
        else:
            if self.find_element(self._automatic_correct_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('自动校正')

    def check_emoji_prediction_capitalization(self, status):
        if status:
            if not (self.find_element(self._emoji_prediction_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('启用表情符号预测')
        else:
            if self.find_element(self._emoji_prediction_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('启用表情符号预测')

    def check_double_click_capitalization(self, status):
        if status:
            if not (self.find_element(self._double_click_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('双击空格键插入句号')
        else:
            if self.find_element(self._double_click_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('双击空格键插入句号')

    def check_quickly_insert_capitalization(self, status):
        if status:
            if not (self.find_element(self._quickly_insert_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('快速插入联想词')
        else:
            if self.find_element(self._quickly_insert_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('快速插入联想词')

    def check_long_press_capitalization(self, status):
        if status:
            if not (self.find_element(self._long_press_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('长按整词删除')
        else:
            if self.find_element(self._long_press_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('长按整词删除')

    def check_experience_plan_capitalization(self, status):
        if status:
            if not (self.find_element(self._experience_plan_capitalization_checkbox).get_attribute('checked')):
                self.find_element_by_text_click('用户体验提升计划')
        else:
            if self.find_element(self._experience_plan_capitalization_checkbox).get_attribute('checked'):
                self.find_element_by_text_click('长用户体验提升计划')
