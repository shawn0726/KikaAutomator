import os
import time

from selenium.webdriver.remote.webelement import WebElement

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
        # 列表方式
        # mlist = self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/iv_add')
        # print(mlist)
        # print(type(mlist))
        # self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/iv_add')[8].click()
        #传入语言
        add_language_name = '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 ' + language + ' 语言"]'
        flag = True
        i = 0
        while flag:
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath(add_language_name).click()
                flag = False
                print("添加语言成功")
            except:
                self.swipeUp(self.driver, n=1)
                i = i+1
                if i == 14:
                   flag = False
                   print("查无此语言")
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
        #取消勾选按序号从上到下 0开始
        mlist = self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/cb_lang')
        print(mlist)
        self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/cb_lang')[0].click()
        #取消语言列表第一个勾选
        # self.find_element_click(self._check_box)
        # #传入语言
        del_language_name = '//android.widget.ImageView[@content-desc="删除语言按键，双击删除 ' + language + ' 语言"]'
        flag = True
        i = 0
        while flag:
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath(del_language_name).click()
                flag = False
                print("删除语言成功")
            except:
                self.swipeUp(self.driver, n=1)
                i = i+1
                if i == 14:
                   flag = False
                   print("查无此语言")

    def update_layout(self, layouttext1):
        mlist = self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/tv_layout')
        print(mlist)
        self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/tv_layout')[0].click()
        #layouttext1为设置布局
        try:
            self.find_element_by_text_click(layouttext1)
            print("更换布局成功")
            time.sleep(2)
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            print("查无此布局")
            time.sleep(1)
            self.driver.find_element_by_id('android:id/button1').click()



