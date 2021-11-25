from selenium.webdriver.common.by import By

from commons.base_function import BaseFunction


class MechanicalKeyboardPage(BaseFunction):
    _id_iv_mechanical_switch = (By.ID, 'com.kika.photon.inputmethod:id/iv_mechanical_switch')
    _xpath_layout_selected = (By.XPATH,
                              '//android.widget.FrameLayout[@content-desc="MOBA Games 3D Mechanical 主题，正在使用"]'
                              '/android.widget.FrameLayout/android.widget.ImageView[3]')

    def tap_back(self):
        self.find_element_by_contenet_des_click('转到上一层级')

    # status 为'on'意为开启，反之，'off'为关闭;开启状态下需要检查：开关是否'checked'，机械轴是否'checked'，布局是否'checked'三种状态
    # 但此处只检查开关与布局是否'checked'，机械轴选中状态的检查在choose_which_axis过程中完成，故不在此处检查
    def tap_mechanical_switch(self, status):
        if status == 'on':
            if self.find_element_by_id('com.kika.photon.inputmethod:id/iv_mechanical_switch').get_attribute('checked') \
                    == "true":
                print('switch already turn on')
            else:
                self.find_element_by_id_click('com.kika.photon.inputmethod:id/iv_mechanical_switch')
                self.driver.implicitly_wait(2)
                if self.find_element_by_id('com.kika.photon.inputmethod:id/iv_mechanical_switch').get_attribute(
                        'checked') == "true":
                    print('turn on')
        if status == 'off':
            if self.find_element_by_id('com.kika.photon.inputmethod:id/iv_mechanical_switch').get_attribute('checked') \
                    == "true":
                self.find_element_by_id_click('com.kika.photon.inputmethod:id/iv_mechanical_switch')
                self.driver.implicitly_wait(2)
                if self.find_element_by_id('com.kika.photon.inputmethod:id/iv_mechanical_switch').get_attribute(
                        'checked') == "false":
                    print('turn off')
            else:
                print('switch already turn off')

    # text 为'青轴'、'红轴'、'黑轴'，3选1
    def choose_which_axis(self, text):
        self.find_element_by_text_click(text)
        if self.find_element_by_text(text).get_attribute('checked') == 'true':
            print('%s 已被选中' % text)
        else:
            print('%s 没被选中' % text)
