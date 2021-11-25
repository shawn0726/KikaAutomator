import time

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class InputSettingPage(BaseFunction):

    def click_which_item(self, which):
        self.driver.find_element_by_xpath('//*[@text="%s"]' % which).click()

    def check_item_status(self, which):
        status = self.driver.find_element_by_xpath(
            '//*[@text="%s"]/../following-sibling::android.widget.LinearLayout/android.widget.CheckBox' % which). \
            get_attribute('checked')
        print('status: ', status)
        return status

