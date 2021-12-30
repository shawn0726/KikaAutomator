from public.base_function import BaseFunction


# 设置-输入设置-中文设置
class ChineseSettingPage(BaseFunction):
    # 模糊拼音
    def fuzzy_pinyin(self, data_list):
        """
        :param data_list: 通过list的方式存放要操作的模糊拼音，填入内容为模糊拼音 item 的 text 属性
        :return:
        """
        self.driver.find_element_by_xpath('//*[@text="模糊拼音"]').click()
        self.driver.implicitly_wait(15)
        for i in data_list:
            self.driver.find_element_by_xpath('//*[@text="%s"]' % i).click()

    def get_fuzzy_pinyin_status(self, which_one):
        """
        :param which_one: 要查看的 item 的 text 属性
        :return:
        """
        status = self.driver.find_element_by_xpath('//*[@text="%s"]/../following-sibling::android.widget.LinearLayout'
                                                   '/android.widget.Switch' % which_one).get_attribute('checked')
        return status

    def get_all_fuzzy_pinyin_status(self):
        false_count = 0
        true_count = 0
        self.driver.find_element_by_xpath('//*[@text="模糊拼音"]').click()
        self.driver.implicitly_wait(15)
        for i in range(2, 12):
            status = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.huawei.ohos.inputmethod:id/recycler_view"]/android.widget.FrameLayout['
                '%d]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch' %
                i).get_attribute('checked')
            self.driver.implicitly_wait(15)
            print('status[%d]:%s' % (i, status))
            if status == 'false':
                false_count += 1
            elif status == 'true':
                true_count += 1
        return false_count, true_count

    # 拼音云输入、混合输入英文单词、上滑输入、繁体输入相关设置
    def chinese_setting_about_input(self, text,  to_do):
        """
        :param text: 拼音云输入、混合输入英文单词、上滑输入、繁体输入
        :param to_do: '开启'、'关闭'
        :return:
        """
        status = self.driver.find_element_by_xpath('//*[@text="%s"]/../following-sibling::android.widget'
                                                   '.LinearLayout/android.widget.Switch' % text).get_attribute('text')
        if status == to_do:
            print('当前开关的状态：', status)
        else:
            self.driver.find_element_by_xpath('//*[@text="%s"]' % text).click()

    # 获取中文设置页面开关状态
    def get_all_status_in_chinese_setting(self, text):
        status = self.driver.find_element_by_xpath('//*[@text="%s"]/../following-sibling::android.widget'
                                                   '.LinearLayout/android.widget.Switch' % text).get_attribute('text')
        return status

    # 双拼输入
    def shuangpin_input(self, which_one):
        """
        :param which_one: '关闭'、'智能ABC'、'微软双拼'、'拼音加加'、'小鹤双拼'、'紫光双拼'、'自然码'、'搜狗双拼'、'取消'
        :return:
        """
        status = self.get_screen_orientation()
        if status == 'PORTRAIT':
            self.driver.find_element_by_xpath('//*[@text="%s"]' % '双拼输入').click()
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_xpath('//*[@text="%s"]' % which_one).click()
        elif status == 'LANDSCAPE':
            self.scroll_to_find('//*[@resource-id="com.huawei.ohos.inputmethod:id/recycler_view"]', '双拼输入')
            self.driver.implicitly_wait(15)
            self.scroll_to_find('//*[@resource-id="android:id/select_dialog_listview"]', which_one)

    def get_shuangpin_input_text(self):
        text = self.driver.find_element_by_xpath('//*[@text="%s"]/following-sibling::android.widget.TextView' %
                                                 '双拼输入').get_attribute('text')
        return text

    # 双拼方案（双拼指南页面是一个imageview，页面上的元素无法定位）
    def shuangpin_plan(self):
        self.driver.find_element_by_xpath('//*[@text="%s"]' % '双拼方案').click()
        self.driver.implicitly_wait(15)
        bounds = self.container_bounds('//*[@text="小艺输入法双拼"]', 'xpath')
        continue_swipe = True
        while continue_swipe:
            before_swipe = self.driver.page_source
            self.driver.swipe((bounds[0] + bounds[2]) / 2,
                              (bounds[3] - 1),
                              (bounds[0] + bounds[2]) / 2,
                              (bounds[1] + bounds[3]) / 2)
            after_swipe = self.driver.page_source
            if after_swipe == before_swipe:
                continue_swipe = False







