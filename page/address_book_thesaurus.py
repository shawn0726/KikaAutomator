from commons.base_function import BaseFunction


class AddressBookThesaurusPage(BaseFunction):
    def tap_the_switch_of_auto_sync_address_book_to_thesaurus(self, to_do):
        """
        :param to_do: 开启、关闭
        :return:
        """
        switch_status = self.find_element_by_xpath('//*[@text="自动同步通讯录到词库"]/../following-sibling::android.widget'
                                                   '.LinearLayout/android.widget.Switch').get_attribute('text')
        if switch_status == to_do:
            print('自动同步通讯录到词库开关状态：', switch_status)
        else:
            self.find_element_by_xpath_click('//*[@text="自动同步通讯录到词库"]')

    def sync_address_book(self):
        self.find_element_by_xpath_click('//*[@text="同步通讯录词库"]')

    def clear_address_book(self, to_do):
        """
        :param to_do: 取消、清空
        :return:
        """
        self.find_element_by_xpath_click('//*[@text="清空通讯录词库"]')
        self.driver.implicitly_wait(15)
        self.find_element_by_xpath_click('//*[@text="%s"]' % to_do)
