import time

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class InputSettingPage(BaseFunction):
    _xpath_locator_input_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _slide_input = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                    'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                    'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                    'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                    'android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.CheckBox')

    _slide_orbit = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                    'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                    'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                    'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                    'android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.CheckBox')

    _auto_capitalization = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/'
                            'android.widget.LinearLayout/android.widget.FrameLayout/'
                            'androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/'
                            'android.widget.LinearLayout/android.widget.CheckBox')

    _suggest_capitalization = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                               'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                               'android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/'
                               'android.widget.LinearLayout/android.widget.FrameLayout/'
                               'androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/'
                               'android.widget.LinearLayout/android.widget.CheckBox')

    _automatic_correct = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                          'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                          'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                          'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                          'android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.CheckBox')

    _emoji_prediction = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                         'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                         'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                         'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                         'android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.CheckBox')

    _double_click = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                     'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                     'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                     'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                     'android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.CheckBox')

    _quickly_insert = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                       'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                       'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                       'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                       'android.widget.LinearLayout[8]/android.widget.LinearLayout/android.widget.CheckBox')

    _long_press = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                   'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                   'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                   'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                   'android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.CheckBox')

    _experience_plan = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                        'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                        'android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                        'android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/'
                        'android.widget.LinearLayout[8]/android.widget.LinearLayout/android.widget.CheckBox')

    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_input_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def check_slide_input_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._slide_input).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._slide_input).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._slide_input).click()
               nowstatus = self.driver.find_element_by_xpath(self._slide_input).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._slide_input).click()
                nowstatus = self.driver.find_element_by_xpath(self._slide_input).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._slide_input).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_slide_orbit_capitalization(self, checkbox):
        nowstatus_slide_input = self.driver.find_element_by_xpath(self._slide_input).get_attribute('checked')
        print(nowstatus_slide_input)
        if nowstatus_slide_input == 'false':
            print("无法勾选")
        if nowstatus_slide_input == 'true':
            print("继续操作")
            nowstatus = self.driver.find_element_by_xpath(self._slide_orbit).get_attribute('checked')
            print(nowstatus)
            if checkbox == 'select':
               if nowstatus == 'true':
                  nowstatus = self.driver.find_element_by_xpath(self._slide_orbit).get_attribute('checked')
                  print('勾选状态为', nowstatus)
               if nowstatus == 'false':
                  self.driver.find_element_by_xpath(self._slide_orbit).click()
                  nowstatus = self.driver.find_element_by_xpath(self._slide_orbit).get_attribute('checked')
                  print('勾选状态为', nowstatus)

            if checkbox == 'noselect':
              if nowstatus == 'true':
                 self.driver.find_element_by_xpath(self._slide_orbit).click()
                 nowstatus = self.driver.find_element_by_xpath(self._slide_orbit).get_attribute('checked')
                 print('勾选状态为', nowstatus)
              if nowstatus == 'false':
                 nowstatus = self.driver.find_element_by_xpath(self._slide_orbit).get_attribute('checked')
                 print('勾选状态为', nowstatus)

    def check_auto_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._auto_capitalization).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._auto_capitalization).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._auto_capitalization).click()
               nowstatus = self.driver.find_element_by_xpath(self._auto_capitalization).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._auto_capitalization).click()
                nowstatus = self.driver.find_element_by_xpath(self._auto_capitalization).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._auto_capitalization).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_suggest_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._suggest_capitalization).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._suggest_capitalization).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._suggest_capitalization).click()
               nowstatus = self.driver.find_element_by_xpath(self._suggest_capitalization).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._suggest_capitalization).click()
                nowstatus = self.driver.find_element_by_xpath(self._suggest_capitalization).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._suggest_capitalization).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_automatic_correct_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._automatic_correct).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._automatic_correct).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._automatic_correct).click()
               nowstatus = self.driver.find_element_by_xpath(self._automatic_correct).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._automatic_correct).click()
                nowstatus = self.driver.find_element_by_xpath(self._automatic_correct).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._automatic_correct).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_emoji_prediction_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._emoji_prediction).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._emoji_prediction).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._emoji_prediction).click()
               nowstatus = self.driver.find_element_by_xpath(self._emoji_prediction).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._emoji_prediction).click()
                nowstatus = self.driver.find_element_by_xpath(self._emoji_prediction).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._emoji_prediction).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_double_click_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._double_click).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._double_click).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._double_click).click()
               nowstatus = self.driver.find_element_by_xpath(self._double_click).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._double_click).click()
                nowstatus = self.driver.find_element_by_xpath(self._double_click).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._double_click).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_quickly_insert_capitalization(self, checkbox):
        nowstatus = self.driver.find_element_by_xpath(self._quickly_insert).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._quickly_insert).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._quickly_insert).click()
               nowstatus = self.driver.find_element_by_xpath(self._quickly_insert).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._quickly_insert).click()
                nowstatus = self.driver.find_element_by_xpath(self._quickly_insert).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._quickly_insert).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_long_press_capitalization(self,checkbox):
        self.swipeUp(self.driver, t=500, n=1)
        nowstatus = self.driver.find_element_by_xpath(self._long_press).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._long_press).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._long_press).click()
               nowstatus = self.driver.find_element_by_xpath(self._long_press).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._long_press).click()
                nowstatus = self.driver.find_element_by_xpath(self._long_press).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._long_press).get_attribute('checked')
                print('勾选状态为', nowstatus)

    def check_experience_plan_capitalization(self, checkbox):
        self.swipeUp(self.driver, t=500, n=1)
        nowstatus = self.driver.find_element_by_xpath(self._experience_plan).get_attribute('checked')
        print(nowstatus)
        if checkbox == 'select':
            if nowstatus == 'true':
                nowstatus = self.driver.find_element_by_xpath(self._experience_plan).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
               self.driver.find_element_by_xpath(self._experience_plan).click()
               nowstatus = self.driver.find_element_by_xpath(self._experience_plan).get_attribute('checked')
               print('勾选状态为', nowstatus)

        if checkbox == 'noselect':
            if nowstatus == 'true':
                self.driver.find_element_by_xpath(self._experience_plan).click()
                nowstatus = self.driver.find_element_by_xpath(self._experience_plan).get_attribute('checked')
                print('勾选状态为', nowstatus)
            if nowstatus == 'false':
                nowstatus = self.driver.find_element_by_xpath(self._experience_plan).get_attribute('checked')
                print('勾选状态为', nowstatus)
