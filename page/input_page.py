import re

from selenium.webdriver.common.by import By

import golVar
from commons.base_function import BaseFunction


class InputPage(BaseFunction):
    _gdpr_join_checkbox = (By.ID, 'com.huawei.ohos.inputmethod:id/cb_join')
    _gdpr_agree_button = (By.ID, 'com.huawei.ohos.inputmethod:id/btn_right')
    _xpath_locator_ohos = (
        By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    _xpath_locator_menu = (By.XPATH, '//*[@resource-id="com.huawei.ohos.inputmethod:id/icon"]')
    _xpath_locator_sound_vibration = (By.XPATH, '//*[@text="音效和振动"]')
    _id_float_kbd_restore = (By.ID, 'com.huawei.ohos.inputmethod:id/float_kbd_restore')
    _id_float_kbd_resize = (By.ID, 'com.huawei.ohos.inputmethod:id/float_kbd_resize')
    _id_float_kbd_move = (By.ID, 'com.huawei.ohos.inputmethod:id/float_kbd_move')
    _id_entry_image_button = (By.ID, 'com.huawei.ohos.inputmethod:id/entry_image_button')
    _xpath_entry_back = (By.XPATH, '//android.widget.ImageView[@content-desc="隐藏键盘"]')

    # 点击键盘左上角menu按钮进入menu菜单，
    def tap_menu(self):
        # self.find_element_by_contenet_des_click('菜单按键。双击打开菜单页面。')
        self.find_element_click(self._id_entry_image_button)

    # 点击键盘右上角返回按钮
    def menu_back(self):
        # self.find_element_by_contenet_des_click('隐藏键盘')
        self.find_element_click(self._xpath_entry_back)

    # 切换键盘布局
    def tap_keyboard_layout(self):
        # self.move_to_find_text('键盘布局')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '键盘布局')

    # 根据当前语言，填写希望切换的布局，如中文：'26键'、'9键'、'笔画'、'手写键盘'
    def to_which_keyboard_layout(self, text):
        # if self.is_element_exist(text):
        #     self.find_element_by_text_click(text)
        # else:
        #     print('当前布局不存在')
        self.find_element_by_xpath_click('//*[@text="%s"]' % text)
        # self.set_layout(text)
        golVar.set_value('language_layout', text)

    # 更改键盘模式
    def tap_keyboard_mode(self):
        # self.move_to_find_text('键盘模式')
        # self.find_element_by_text_click('键盘模式')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '键盘模式')

    # 根据当前语言，填写希望切换的键盘模式，如中文：'普通键盘'、'单手模式'、'悬浮键盘'、'拇指模式'
    def to_which_keyboard_mode(self, text):
        # if self.is_element_exist(text):
        #     self.find_element_by_text_click(text)
        # else:
        #     print('当前模式不存在')
        self.find_element_by_xpath_click('//*[@text="%s"]' % text)

    # 单手键盘右手与左手键盘模式相互切换键
    def switch_keyboard_to_opposite(self):
        # self.find_element_by_contenet_des_click('左手键盘。双击切换为左手键盘。')
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/one_hand_switch').click()

    # 单手键盘还原为普通键盘
    def return_to_normal(self):
        # self.find_element_by_contenet_des_click('标准键盘尺寸按钮。双击切换为标准键盘。')com.huawei.ohos.inputmethod:id/one_hand_size
        self.driver.find_element_by_id('com.huawei.ohos.inputmethod:id/one_hand_size').click()

    # 点击悬浮键盘还原按钮，还原至普通键盘模式
    def float_to_normal(self):
        self.find_element_click(self._id_float_kbd_restore)

    # 点击悬浮键盘上的'大小调节'按钮，进行大小调节操作
    def tap_float_to_resize(self):
        self.find_element_click(self._id_float_kbd_resize)

    '''上下左右，4个按钮，分别以'a'、'b'、'c'、'd'代替, steps 为int类型，以10个单位的速率移动,上边界在y轴方向最大移动距离为（130/屏幕分辨率）个单位，故 a 向上移动（10/屏幕分辨率）个单位，b 
    最多只能向下移动（120/屏幕分辨率）个单位，目前只粗略估算，统一认为上下边界移动最大距离为（130/屏幕分辨率）个单位，一旦上下边界移动距离达（130
    /屏幕分辨率）个单位，再进行扩大移动，边界距离不再扩大，检验逻辑到此可行，故未进行更细致考虑 '''

    def float_to_resize(self, which, direction, steps, vm_x, vm_y):
        ll_drag_shadow_bounds = self.container_bounds('ll_drag_shadow', 'resource_id')
        sx, sy, ex, ey = ll_drag_shadow_bounds[0], ll_drag_shadow_bounds[1], \
                         ll_drag_shadow_bounds[2], ll_drag_shadow_bounds[3]
        a_x = (sx + ex) / 2
        a_y = sy
        c_x = sx
        c_y = (sy + ey) / 2
        b_x = (sx + ex) / 2
        b_y = ey
        d_x = ex
        d_y = (sy + ey) / 2
        # windows_x = self.driver.get_window_size()['width']
        # windows_y = self.driver.get_window_size()['height']
        if which == 'a':
            if direction == 'up':
                self.driver.swipe(a_x, a_y + 1, a_x, a_y - min(10 * steps, a_y))
            if direction == 'down':
                self.driver.swipe(a_x, a_y + 1, a_x, a_y + min(10 * steps, (130 * vm_y) / 1520))
        if which == 'b':
            if direction == 'up':
                self.driver.swipe(b_x, b_y - 1, b_x, b_y - min(10 * steps, a_y))
            if direction == 'down':
                print(b_x, b_y, b_x, b_y + min(min(10 * steps, (130 * vm_y) / 1520), vm_y - b_y))
                self.driver.swipe(b_x, b_y - 1, b_x,
                                  b_y - 1 + min(min(10 * steps, (130 * vm_y) / 1520), vm_y - b_y))
        if which == 'c':
            if direction == 'left':
                self.driver.swipe(c_x + 1, c_y, c_x - min(10 * steps, c_x), c_y)
            if direction == 'right':
                self.driver.swipe(c_x + 1, c_y, c_x + min(10 * steps, (141 * vm_x) / 720), c_y)
        if which == 'd':
            if direction == 'left':
                self.driver.swipe(d_x - 1, d_y, d_x - min(10 * steps, d_x), d_y)
            if direction == 'right':
                self.driver.swipe(d_x - 1, d_y,
                                  d_x - 1 + min(min(10 * steps, (141 * vm_x) / 720), vm_x - d_x), d_y)

        def float_to_resize1(self, which, direction, steps, vm_x, vm_y):
            ll_drag_shadow_bounds = self.container_bounds('ll_drag_shadow', 'resource_id')
            sx, sy, ex, ey = ll_drag_shadow_bounds[0], ll_drag_shadow_bounds[1], \
                             ll_drag_shadow_bounds[2], ll_drag_shadow_bounds[3]
            a_x = (sx + ex) / 2
            a_y = sy
            c_x = sx
            c_y = (sy + ey) / 2
            b_x = (sx + ex) / 2
            b_y = ey
            d_x = ex
            d_y = (sy + ey) / 2
            windows_x = self.driver.get_window_size()['width']
            windows_y = self.driver.get_window_size()['height']
            available_distance_expand = (502 - (ey - sy)) * vm_y / 1520
            available_distance_reduce = ((ey - sy) - 372) * vm_y / 1520
            if which == 'a':
                if direction == 'up':
                    self.driver.swipe(a_x, a_y + 1, a_x, a_y - min(min(10 * steps, a_y), available_distance_expand))
                if direction == 'down':
                    self.driver.swipe(a_x, a_y + 1, a_x, a_y + min(10 * steps, available_distance_reduce))
            if which == 'b':
                if direction == 'up':
                    self.driver.swipe(b_x, b_y - 1, b_x, b_y - min(10 * steps, available_distance_reduce))
                if direction == 'down':
                    print(b_x, b_y, b_x, b_y + min(min(10 * steps, available_distance_expand), windows_y - b_y))
                    self.driver.swipe(b_x, b_y - 1, b_x,
                                      b_y - 1 + min(min(10 * steps, available_distance_expand), windows_y - b_y))
            if which == 'c':
                if direction == 'left':
                    self.driver.swipe(c_x + 1, c_y, c_x - min(10 * steps, c_x), c_y)
                if direction == 'right':
                    self.driver.swipe(c_x + 1, c_y, c_x + min(10 * steps, (141 * vm_x) / 720), c_y)
            if which == 'd':
                if direction == 'left':
                    self.driver.swipe(d_x - 1, d_y, d_x - min(10 * steps, d_x), d_y)
                if direction == 'right':
                    self.driver.swipe(d_x - 1, d_y,
                                      d_x - 1 + min(min(10 * steps, (141 * vm_x) / 720), windows_x - d_x), d_y)

    # 点击悬浮键盘上的'恢复默认'按钮，恢复到默认设置
    def float_restore_default(self):
        self.find_element_by_xpath_click('//*[@resource-id="com.huawei.ohos.inputmethod:id/%s"]' % 'restore_default')

    # 点击悬浮键盘上的'确认'按钮，确认设置。双击保存当前键盘尺寸
    def float_finish_resize(self):
        self.find_element_by_xpath_click('//*[@resource-id="com.huawei.ohos.inputmethod:id/%s"]' % 'finish_resize')

    def float_to_move(self, direction, steps):
        # 悬浮键盘共分：上、中、下，3部分，移动至边界时，移动的最大值需要考虑到容器的高度与宽度
        # top 部分
        float_extra_container_top = self.container_bounds('extra_container_top', 'resource_id')
        float_extra_container_top_hight = float_extra_container_top[3] - float_extra_container_top[1]
        # 中间部分
        float_extra_container_middle = self.container_bounds('keyboard_root_container', 'resource_id')
        float_extra_container_middle_hight = float_extra_container_middle[3] - float_extra_container_middle[1]
        # 底部
        float_extra_container_bottom = self.container_bounds('extra_container_bottom', 'resource_id')
        float_extra_container_bottom_hight = float_extra_container_bottom[3] - float_extra_container_bottom[1]
        # 首先获取悬浮按钮的位置
        float_kbd_move_bounds = self.find_element_by_xpath(
            '//*[@resource-id="com.huawei.ohos.inputmethod:id/float_kbd_move"]').get_attribute('bounds')
        bounds_string_to_array = re.findall(r'\d+', float_kbd_move_bounds)
        sx, sy, ex, ey = float(bounds_string_to_array[0]), float(bounds_string_to_array[1]), \
                         float(bounds_string_to_array[2]), float(bounds_string_to_array[3])
        mx = (sx + ex) / 2
        my = (sy + ey) / 2
        print('***这是：', sx, sy, ex, ey, mx, my)
        if direction == 'up':
            last_y = my - min(steps * (my - sy), float_extra_container_top[1] - float_extra_container_top_hight / 2)
            self.driver.swipe(mx, my, mx, last_y)
        if direction == 'down':
            windows_y = self.driver.get_window_size()['height']
            last_y = my + min(my + steps * (ey - my), windows_y - float_extra_container_top_hight / 2 -
                              float_extra_container_middle_hight - float_extra_container_bottom_hight)
            self.driver.swipe(mx, my, mx, last_y)
        if direction == 'left':
            # 向左移动的最大距离为容器左侧到手机屏幕左侧距离之差
            last_x = mx - min(steps * (mx - sx), float_extra_container_top[0])
            self.driver.swipe(mx, my, last_x, my)
        if direction == 'right':
            # 向右移动的最大距离为容器最右端到手机屏幕右侧的距离之差
            windows_x = self.driver.get_window_size()['width']
            last_x = mx + min(steps * (ex - mx), (windows_x - float_extra_container_middle[2]))
            self.driver.swipe(mx, my, last_x, my)

    # 更改主题
    def change_theme(self):
        # self.move_to_find_text('主题')
        # self.find_element_by_text_click('主题')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '主题')
        from page.theme_setting_page import ThemeSettingPage
        return ThemeSettingPage(self.driver)

    # 编辑键盘-调节尺寸大小
    def tap_adjust_size(self):
        # self.move_to_find_text('编辑键盘')
        # self.find_element_by_text_click('编辑键盘')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '编辑键盘')

    def adjust_size(self, which, direction, steps, vm_x, vm_y):
        # 上下左右，4个按钮，分别以'a'、'b'、'c'、'd'代替
        ll_drag_shadow_bounds = self.container_bounds('ll_drag_shadow', 'resource_id')
        sx, sy, ex, ey = ll_drag_shadow_bounds[0], ll_drag_shadow_bounds[1], \
                         ll_drag_shadow_bounds[2], ll_drag_shadow_bounds[3]
        a_x = (sx + ex) / 2
        a_y = sy
        c_x = sx
        c_y = (sy + ey) / 2
        b_x = (sx + ex) / 2
        b_y = ey
        d_x = ex
        d_y = (sy + ey) / 2
        available_distance_expand = ((642 - ey + sy) * float(vm_y)) / 1520
        available_distance_reduce = ((ey - sy - 428) * float(vm_y)) / 1520
        windows_x = self.driver.get_window_size()['width']
        windows_y = self.driver.get_window_size()['height']
        if which == 'a':
            if direction == 'up':
                self.driver.swipe(a_x, a_y + 1, a_x, a_y - min(min(10 * steps, a_y), available_distance_expand))
            if direction == 'down':
                self.driver.swipe(a_x, a_y + 1, a_x, a_y + min(10 * steps, available_distance_reduce))
        if which == 'b':
            if direction == 'up':
                self.driver.swipe(b_x, b_y - 1, b_x, b_y - min(10 * steps, available_distance_reduce))
            if direction == 'down':
                print(b_x, b_y, b_x, b_y + min(min(10 * steps, available_distance_expand), windows_y - b_y))
                self.driver.swipe(b_x, b_y - 1, b_x,
                                  b_y - 1 + min(min(10 * steps, available_distance_expand), windows_y - b_y))
        if which == 'c':
            if direction == 'left':
                self.driver.swipe(c_x + 1, c_y, c_x - min(10 * steps, c_x), c_y)
            if direction == 'right':
                self.driver.swipe(c_x + 1, c_y, c_x + min(10 * steps, (216 * float(vm_x)) / 720), c_y)
        if which == 'd':
            if direction == 'left':
                self.driver.swipe(d_x - 1, d_y, d_x - min(10 * steps, d_x), d_y)
            if direction == 'right':
                self.driver.swipe(d_x - 1, d_y,
                                  d_x - 1 + min(min(10 * steps, (216 * float(vm_x)) / 720), windows_x - d_x), d_y)

    def adjust_move(self, direction, steps, vm_y):
        ll_drag_shadow_bounds = self.container_bounds('ll_drag_shadow', 'resource_id')
        sx, sy, ex, ey = ll_drag_shadow_bounds[0], ll_drag_shadow_bounds[1], \
                         ll_drag_shadow_bounds[2], ll_drag_shadow_bounds[3]
        a_x = (sx + ex) / 2
        c_x = sx
        b_y = ey
        d_x = ex
        d_y = (sy + ey) / 2
        available_distance_expand = (sy - 599) * float(vm_y) / 1520
        windows_x = self.driver.get_window_size()['width']
        windows_y = self.driver.get_window_size()['height']
        if direction == 'up':
            self.driver.swipe(a_x, d_y, a_x, d_y - min(10 * steps, available_distance_expand))
        if direction == 'down':
            self.driver.swipe(a_x, d_y, a_x, d_y + min(10 * steps, windows_y - b_y))
        if direction == 'left':
            self.driver.swipe(a_x, d_y, a_x - min(10 * steps, c_x), d_y)
        if direction == 'right':
            self.driver.swipe(a_x, d_y, a_x + min(10 * steps, windows_x - d_x), d_y)

    # 剪切板
    def tap_clipboard(self):
        self.find_element_by_xpath_click('//*[@text="%s"]' % '剪贴板')

    # 剪切板内容最多显示 3 条，which_one = 1 / 2 / 3
    def clipboard_func(self, which_one, do_what):
        # self.move_to_find_text('剪贴板')
        # self.find_element_by_text_click('剪贴板')
        # self.find_element_click(self._xpath_clipboard_data)
        self.find_element_by_xpath_click('//*[@resource-id="com.huawei.ohos.inputmethod:id/recycler_view"]/android'
                                         '.widget.FrameLayout[%d]' % which_one)
        if do_what == '粘贴':
            resource_id = 'button_paste'
        if do_what == '移除':
            resource_id = 'button_remove'
        if do_what == '取消':
            resource_id = 'button_cancel'
        self.find_element_by_xpath_click('//*[@resource-id="com.huawei.ohos.inputmethod:id/%s"]' % resource_id)

    # 编辑-全选、复制、粘贴、剪切板
    def tap_edit(self):
        # self.move_to_find_text('编辑')
        # self.find_element_by_text_click('编辑')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '编辑')

    '''
        使用选择器时，选中'选择'按钮后，点击方向键选中字符，注意要从前往后，从后往前 appium 会报错
    '''

    # do_what 为编辑页面中对应的按钮操作，具体值见下方 value 部分
    def edit_operation(self, do_what):
        choice_round_bounds = self.container_bounds('choice_round', 'resource_id')
        sx1, sy1, ex1, ey1 = choice_round_bounds[0], choice_round_bounds[1], \
                             choice_round_bounds[2], choice_round_bounds[3]
        choice_text_bounds = self.container_bounds('choice_text', 'resource_id')
        sx2, sy2, ex2, ey2 = choice_text_bounds[0], choice_text_bounds[1], \
                             choice_text_bounds[2], choice_text_bounds[3]
        up_x = (sx1 + ex1) / 2
        up_y = (sy1 + sy2) / 2
        down_x = (sx1 + ex1) / 2
        down_y = (ey1 + ey2) / 2
        left_x = (sx1 + sx2) / 2
        left_y = (sy1 + ey1) / 2
        right_x = (ex1 + ex2) / 2
        right_y = (sy1 + ey1) / 2
        if do_what == 'up':
            self.driver.tap([(up_x, up_y)])
            return
        if do_what == 'down':
            self.driver.tap([(down_x, down_y)])
            return
        if do_what == 'left':
            self.driver.tap([(left_x, left_y)])
            return
        if do_what == 'right':
            self.driver.tap([(right_x, right_y)])
            return
        if do_what == '全选':
            resource_id = 'selectall_text'
        if do_what == '剪切':
            resource_id = 'selectall_text'
        if do_what == '删除':
            resource_id = 'delete_image'
        if do_what == '复制':
            resource_id = 'copy_text'
        if do_what == '回车':
            resource_id = 'enter_image_relay'
        if do_what == '粘贴':
            resource_id = 'paste_text'
        if do_what == '剪切板':
            resource_id = 'clipboard_text'
        if do_what == '句首':
            resource_id = 'choice_left_image'
        if do_what == '句尾':
            resource_id = 'choice_right_image_relay'
        if do_what == '选择':
            resource_id = 'choice_text'
        self.find_element_by_xpath_click('//*[@resource-id="com.huawei.ohos.inputmethod:id/%s"]' % resource_id)

    # 点击音效和振动
    def tap_sound_vibration(self):
        # self.find_element_click(self._xpath_locator_sound_vibration)
        self.find_element_by_xpath_click('//*[@text="%s"]' % '音效和振动')
        # self.move_to_find_text('音效和振动')
        # self.find_element_by_text_click('音效和振动')

    # 机械键盘
    def tap_mechanical_keyboard(self):
        # self.move_to_find_text('机械键盘')
        # self.find_element_by_text('机械键盘').location_once_scrolled_into_view()
        # self.find_element_by_text_click('机械键盘')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '机械键盘')
        from page.mechanical_keyboard_page import MechanicalKeyboardPage
        return MechanicalKeyboardPage(self.driver)

    # 点击设置
    def tap_setting(self):
        # self.move_to_find_text('设置')
        self.find_element_by_xpath_click('//*[@text="%s"]' % '设置')
        # self.find_element_by_text_click('设置')
        from page.keyboard_setting_page import KeyboardSettingPage
        return KeyboardSettingPage(self.driver)

    # 调整振动 percent 为占比，如：0.5
    def adjust_vibration(self, percent):
        vibration_adjust_bounds = self.container_bounds('按键振动', 'xpath')
        s_x, s_y, e_x, e_y = vibration_adjust_bounds[0], vibration_adjust_bounds[1], \
                             vibration_adjust_bounds[2], vibration_adjust_bounds[3]
        m_y = (s_y + e_y) / 2
        width = e_x - s_x
        self.driver.tap([(percent * width, m_y)])

    # 调整音量 percent 为占比，如：0.5
    def adjust_sound(self, percent):
        sound_adjust_bounds = self.container_bounds('按键音量', 'xpath')
        s_x, s_y, e_x, e_y = sound_adjust_bounds[0], sound_adjust_bounds[1], \
                             sound_adjust_bounds[2], sound_adjust_bounds[3]
        m_y = (s_y + e_y) / 2
        width = e_x - s_x
        self.driver.tap([(percent * width, m_y)])

    # 进入音量调节页面
    def enter_keyboard_sound_page(self):
        # try:
        #     self.find_element_by_xpath_click('//*[@text="按键音效"]')
        # except:
        container_bounds = self.container_bounds('recycler_view', 'resource_id')
        self.driver.swipe((container_bounds[0] + container_bounds[2]) / 2,
                          (container_bounds[3] - 1),
                          (container_bounds[0] + container_bounds[2]) / 2,
                          (container_bounds[1] + 1))
        self.driver.find_element_by_xpath('//*[@text="%s"]' % '按键音效').click()
        from page.sound_effect_page import SoundEffectPage
        return SoundEffectPage(self.driver)  # KeyboardSoundPage

    # 长按语言切换按钮，弹出的语言框，若未找到对应元素则滑动再次查询，直到滑动到底部
    def language_picker_list(self, which_one):
        language_picker_list_bounds = self.container_bounds('kbb_language_picker_list', 'resource_id')
        continue_swipe = True
        while continue_swipe:
            try:
                self.driver.find_element_by_xpath('//*[@text="%s"]' % which_one).click()
                continue_swipe = False
            except:
                before_swipe = self.driver.page_source
                self.driver.swipe((language_picker_list_bounds[0] + language_picker_list_bounds[2]) / 2,
                                  (language_picker_list_bounds[3] - 1),
                                  (language_picker_list_bounds[0] + language_picker_list_bounds[2]) / 2,
                                  (language_picker_list_bounds[1] + 1))
                after_swipe = self.driver.page_source
                if after_swipe == before_swipe:
                    continue_swipe = False

    def deal_sys_dialog(self, which_one, do_what):
        if self.is_element_exist(which_one):
            self.driver.find_element_by_xpath('//*[@text="%s"]' % do_what).click()

    def set_default_inputmethod(self, name):
        if name == 'ziyan':
            inputmethod = 'com.huawei.ohos.inputmethod/com.android.inputmethod.latin.LatinIME'
        self.driver.activate_ime_engine(inputmethod)

    def deal_gdpr_informal(self):
        if self.is_element_exist('Celia Keyboard'):
            self.find_element_click(self._gdpr_join_checkbox)
            self.find_element_click(self._gdpr_agree_button)


