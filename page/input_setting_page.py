from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class InputSettingPage(BaseFunction):
    _xpath_locator_input_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _slide_input_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'androidx.recyclerview.widget.RecyclerView/'
                                                      'android.widget.LinearLayout[1]/android.widget.RelativeLayout')
    _slide_orbit_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                      'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout/'
                                                      'androidx.recyclerview.widget.RecyclerView/'
                                                      'android.widget.LinearLayout[2]/android.widget.RelativeLayout')
    _auto_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.view.ViewGroup/'
                                               'android.widget.RelativeLayout/android.widget.FrameLayout/'
                                               'android.widget.LinearLayout/android.widget.FrameLayout/'
                                               'androidx.recyclerview.widget.RecyclerView/'
                                               'android.widget.LinearLayout[3]/android.widget.RelativeLayout')
    _suggest_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                  'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                  'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                  'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                  'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                  'android.widget.FrameLayout/'
                                                  'androidx.recyclerview.widget.RecyclerView/'
                                                  'android.widget.LinearLayout[4]/android.widget.RelativeLayout')
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
                                                           'android.widget.RelativeLayout')
    _double_click_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                       'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                       'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                       'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                       'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                       'android.widget.FrameLayout/'
                                                       'androidx.recyclerview.widget.RecyclerView/'
                                                       'android.widget.LinearLayout[7]/android.widget.RelativeLayout')
    _quickly_insert_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                         'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                         'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                         'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                         'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                         'android.widget.FrameLayout/'
                                                         'androidx.recyclerview.widget.RecyclerView/'
                                                         'android.widget.LinearLayout[8]/android.widget.RelativeLayout')
    _long_press_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                     'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                     'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                     'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                     'android.widget.FrameLayout/'
                                                     'androidx.recyclerview.widget.RecyclerView/'
                                                     'android.widget.LinearLayout[7]/android.widget.RelativeLayout')
    _experience_plan_capitalization_checkbox = (By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                          'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                          'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                          'android.view.ViewGroup/android.widget.RelativeLayout/'
                                                          'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                          'android.widget.FrameLayout/'
                                                          'androidx.recyclerview.widget.RecyclerView/'
                                                          'android.widget.LinearLayout[8]/android.widget.RelativeLayout')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_input_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_slide_input_capitalization(self):
        self.find_element_click(self._slide_input_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_slide_orbit_capitalization(self):
        self.find_element_click(self._slide_orbit_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_auto_capitalization(self):
        self.find_element_click(self._auto_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_suggest_capitalization(self):
        self.find_element_click(self._suggest_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_automatic_correct_capitalization(self):
        self.find_element_click(self._automatic_correct_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_emoji_prediction_capitalization(self):
        self.find_element_click(self._emoji_prediction_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_double_click_capitalization(self):
        self.find_element_click(self._double_click_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_quickly_insert_capitalization(self):
        self.find_element_click(self._quickly_insert_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_long_press_capitalization(self):
        self.swipeUp(self.driver, t=500, n=1)
        self.find_element_click(self._long_press_capitalization_checkbox)
        return InputSettingPage(self.driver)

    def check_experience_plan_capitalization(self):
        self.swipeUp(self.driver, t=500, n=1)
        self.find_element_click(self._experience_plan_capitalization_checkbox)
        return InputSettingPage(self.driver)
