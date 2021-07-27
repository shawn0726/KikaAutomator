import os
import time

from commons.base_function import BaseFunction
from selenium.webdriver.common.by import By


class LanguageSettingPage(BaseFunction):
    _xpath_locator_language_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _open_menu_search_box = (By.ID, 'com.huawei.ohos.inputmethod:id/menu_search_view')
    _close_menu_search_box = (By.ID, 'com.huawei.ohos.inputmethod:id/toolbar_close')
   #_add_language_afrikaans = (By.XPATH, '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 南非荷兰文 语言"]')
   #_add_language_asturianu = (By.XPATH, '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 阿斯图里亚斯文 语言"]')
    _check_box = (By.CLASS_NAME, 'android.widget.CheckBox')


    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_language_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    def open_input_menu_search(self):
        self.find_element_click(self._open_menu_search_box)
        return LanguageSettingPage(self.driver)

    def close_input_menu_search(self):
        self.find_element_click(self._close_menu_search_box)
        return LanguageSettingPage(self.driver)

    def add_language_list(self, language, predict):
        #传入语言
        add_language_name = '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 ' + language + ' 语言"]'
        self.driver.find_element_by_xpath(add_language_name).click()
        #等待下载
        time.sleep(2)
        #返回词典列表
        readtext = os.popen('adb shell "cd /data/data/com.huawei.ohos.inputmethod/files/dictServer && ls"')
        dictext = readtext.read()
        readtext.close()
        #print(dictext)
        print(dictext.strip().split('\n'))
        if predict in dictext.strip().split('\n'):
            print("词典下载成功")
        else:
            print("词典下载失败")
        return predict

    def del_language_list(self, language):
        #取消语言列表第一个勾选
        self.find_element_click(self._check_box)
        #传入语言
        del_language_name = '//android.widget.ImageView[@content-desc="删除语言按键，双击删除 ' + language + ' 语言"]'
        self.driver.find_element_by_xpath(del_language_name).click()

    def update_layout(self, layouttext1):
        self.find_element_by_id('com.huawei.ohos.inputmethod:id/tv_layout').click()
        self.find_element_by_text_click(layouttext1)

        #获取元素
        #text_vlaue = self.driver.find_elements_by_class_name('android.widget.CheckedTextView')
        # # 打印页面中class_name为android.widget.TextView元素的文本内容
        # for i in text_vlaue:
        #     print(i.text)


