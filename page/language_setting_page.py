import os
import time

from selenium.webdriver.remote.webelement import WebElement

from public.base_function import BaseFunction
from selenium.webdriver.common.by import By


class LanguageSettingPage(BaseFunction):
    _xpath_locator_language_setting_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    _open_menu_search_box = (By.ID, 'com.huawei.ohos.inputmethod:id/menu_search_view')
    _close_menu_search_box = (By.ID, 'com.huawei.ohos.inputmethod:id/toolbar_close')
    # _add_language_afrikaans = (By.XPATH, '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 南非荷兰文 语言"]')
    # _add_language_asturianu = (By.XPATH, '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 阿斯图里亚斯文 语言"]')
    _check_box = (By.CLASS_NAME, 'android.widget.CheckBox')

    # 进入设置页面
    def back_to_setting_page(self):
        self.find_element_click(self._xpath_locator_language_setting_back)
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    # 返回上一个页面
    def back_to_previous_page(self):
        self.driver.back()

    # 点击语言列表页面中的搜索符号，展示搜索框，弹起键盘
    def click_input_menu_search(self):
        self.find_element_click(self._open_menu_search_box)

    # 通过搜索框搜索
    def open_input_menu_search(self, text):
        self.find_element_click(self._open_menu_search_box)
        # return LanguageSettingPage(self.driver)
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/search_editor').send_keys(text)
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@text="%s"]/../following-sibling::android.widget.FrameLayout' % text).click()

    # 退出搜索框
    def close_input_menu_search(self):
        self.find_element_click(self._close_menu_search_box)
        return LanguageSettingPage(self.driver)

    # 添加语言
    def add_language_list(self, language, predict):
        # 列表方式
        # mlist = self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/iv_add')
        # print(mlist)
        # print(type(mlist))
        # self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/iv_add')[8].click()
        # 传入语言
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
                i = i + 1
                if i == 14:
                    flag = False
                    print("查无此语言")
        # 等待下载
        time.sleep(2)
        # 返回词典列表
        readtext = os.popen('adb shell "cd /data/data/com.huawei.ohos.inputmethod/files/dictServer && ls"')
        dictext = readtext.read()
        readtext.close()
        # print(dictext)
        print(dictext.strip().split('\n'))
        if predict in dictext.strip().split('\n'):
            print("词典下载成功")
        else:
            print("词典下载失败")
        return predict

    # 添加语言方式2(针对root机型)
    def add_language_list2(self, language, predict):
        language_list_bounds = self.container_bounds('main_list_view', 'resource_id')
        continue_swipe = True
        while continue_swipe:
            try:
                self.driver.find_element_by_xpath(
                    '//android.widget.ImageView[@content-desc="添加语言按键，双击添加 %s 语言"]' % language).click()
                continue_swipe = False
            except:
                before_swipe = self.driver.page_source
                self.driver.swipe((language_list_bounds[0] + language_list_bounds[2]) / 2,
                                  (language_list_bounds[3] - 1),
                                  (language_list_bounds[0] + language_list_bounds[2]) / 2,
                                  (language_list_bounds[1] + language_list_bounds[3]) / 2, 2500)
                after_swipe = self.driver.page_source
                if after_swipe == before_swipe:
                    continue_swipe = False
        # 等待下载
        time.sleep(2)
        # 返回词典列表
        readtext = os.popen('adb shell "su -c cd /data/data/com.huawei.ohos.inputmethod/files/dictServer && ls"')
        dictext = readtext.read()
        readtext.close()
        # print(dictext)
        print(dictext.strip().split('\n'))
        if predict in dictext.strip().split('\n'):
            print("词典下载成功")
        else:
            print("词典下载失败")
        return predict

    # 取消勾选指定语言
    def uncheck_language_list(self, language):
        self.driver.find_element_by_xpath(
            '//*[@text="%s"]/preceding-sibling::android.widget.CheckBox' % language).click()

    # 点击删除按钮，删除指定语言
    def delete_language(self, language):
        self.driver.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="删除语言按键，双击删除 %s 语言"]' % language).click()

    def del_language_list(self, language):
        # 取消勾选按序号从上到下 0开始
        mlist = self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/cb_lang')
        print(mlist)
        self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/cb_lang')[0].click()
        # 取消语言列表第一个勾选
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
                i = i + 1
                if i == 14:
                    flag = False
                    print("查无此语言")

    # 切换布局
    def update_layout(self, layouttext1):
        mlist = self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/tv_layout')
        print(mlist)
        self.driver.find_elements_by_id('com.huawei.ohos.inputmethod:id/tv_layout')[0].click()
        # layouttext1为设置布局
        try:
            self.find_element_by_text_click(layouttext1)
            print("更换布局成功")
            time.sleep(2)
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            print("查无此布局")
            time.sleep(1)
            self.driver.find_element_by_id('android:id/button1').click()

    # 切换布局方式2
    def updata_layout2(self, language, which_one):
        self.driver.find_element_by_xpath(
            '//*[@text="%s"]/../following-sibling::android.widget.RelativeLayout/'
            'android.widget.TextView' % language).click()
        list_num = self.get_list_total_num('//*[@resource-id="%s"]' % 'android:id/select_dialog_listview')
        self.driver.find_element_by_xpath('//*[@resource-id="android:id/select_dialog_listview"]/android.widget'
                                          '.CheckedTextView[%d]' % which_one).click()
        self.driver.find_element_by_xpath('//*[@text="%s"]' % '确定').click()

    # 返回指定语言的勾选状态
    def check_the_language_states(self, name):
        state = self.driver.find_element_by_xpath(
            '//*[@text="%s"]/preceding-sibling::android.widget.CheckBox' % name). \
            get_attribute('checked')
        print('state:', state)
        return state
