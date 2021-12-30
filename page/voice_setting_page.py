from public.base_function import BaseFunction


class VoiceSettingPage(BaseFunction):
    # 语音长文本模式操作
    def operate_extended_dictation(self, operation):
        status = self.find_element_by_xpath('//*[@text="%s"]/../following-sibling::android.widget.LinearLayout'
                                            '/android.widget.Switch' % '语音长文本模式').get_attribute('checked')
        if operation is not status:
            self.find_element_by_xpath('//*[@text="%s"]/../following-sibling::android.widget.LinearLayout'
                                       '/android.widget.Switch' % '语音长文本模式').click()

    # 获取语音长文本模式状态
    def get_extended_dictation_status(self):
        status = self.find_element_by_xpath('//*[@text="%s"]/../following-sibling::android.widget.LinearLayout'
                                            '/android.widget.Switch' % '语音长文本模式').get_attribute('checked')
        return status
