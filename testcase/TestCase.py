import re
import time
from multiprocessing import Pool
import os

import allure
import pytest
from selenium.webdriver.common.by import By

from commons.get_path import get_path_data
from page.input_page import InputPage
from util.device_data import get_vm_size


'''
生成allure报告 2 步：
1、python3 -m pytest testcase/TestCase.py --alluredir report/allure_raw
2、allure generate report/allure_raw -o report/html --clean
'''

screen_size_list = []
test_case_data = get_path_data('/data/case_data.yml')
test_adb_data = get_path_data('/data/adb_data.yml')

# 设置页面右上角back键
_xpath_locator_setting_back = (By.XPATH,
                               '//android.widget.ImageButton[@content-desc="转到上一层级"]')
# GDPR 弹窗相关控件
_gdpr_pop_up = (
    By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
_gdpr_disagree = (By.ID,
                  'com.huawei.ohos.inputmethod:id/btn_deny')
_gdpr_agree = (By.ID,
               'com.huawei.ohos.inputmethod:id/btn_ok')
_gdpr_learn_more = (By.ID, 'com.huawei.ohos.inputmethod:id/tv_content2')
_input_text_view = (By.CLASS_NAME, 'android.widget.EditText')
_message_input_box = (By.ID, 'com.google.android.apps.messaging:id/compose_message_text')
_address_book_dialog = (By.ID, 'com.android.packageinstaller:id/dialog_container')


@allure.story('英文键盘，输字母后删除')
@pytest.mark.parametrize('case_number', [0])
# 通过 case_number 在 case_id 表中查询，对应的 case 使用哪个 driver
def test_InputMethod_SCB_func_01_01_01_0001(get_device_id_list, get_driver_pool, deliver_event,
                                            case_number):
    device_id_list = get_device_id_list
    # pool 池中 driver 与 device_id 为一对一的关系
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(test_adb_data['adb_01_01_01_0003']['emptyinput'] % device_id_list[which_driver_pool])
    time.sleep(1)
    os.system(test_adb_data['adb_01_01_01_0004']['upkeyboard'] % device_id_list[which_driver_pool])
    time.sleep(3)
    if input_page.find_element_by_id('com.android.packageinstaller:id/dialog_container'):
        input_page.find_element_by_id_click('com.android.packageinstaller:id/permission_allow_button')
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('enter', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])

    input_page.input_characters(test_case_data['func_01_01_01_0001']['word1'], device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.input_characters(',', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters(test_case_data['func_01_01_01_0001']['word2'], device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_class("android.widget.EditText").text
    print(text)
    assert text == 'hello ,worl'
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('检查首字母大写功能')
@pytest.mark.parametrize('case_number', [1])
def test_InputMethod_SCB_func_01_01_01_0003(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    os.system(
        test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.google.android.apps.messaging:id/compose_message_text')
    # 有的手机首次调起键盘后，可能会弹起'获取联系人权限'的系统弹框
    # os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    time.sleep(2)
    input_page.find_element_by_id_click(
        'com.android.mms:id/embedded_text_editor')  # com.google.android.apps.messaging:id/compose_message_text
    if input_page.find_element_by_id('com.android.packageinstaller:id/dialog_container'):
        input_page.find_element_by_id_click('com.android.packageinstaller:id/permission_allow_button')
        input_page.find_element_by_id_click('com.google.android.apps.messaging:id/compose_message_text')
    # 检查键盘，非中文键盘，点击'切换'键，切换为英文键盘，检查完后点击enter清空文本框内容，再进行输入
    if input_page.check_language(device_id_list[which_driver_pool], screen_size_list[0],
                                 screen_size_list[1]) == 'english':
        print('当前为英文键盘')
    else:
        input_page.input_characters('switch', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
        input_page.input_characters('delete', device_id_list[which_driver_pool], screen_size_list[0],
                                    screen_size_list[1])
    input_page.input_characters(test_case_data['func_01_01_01_0003']['word'], device_id_list[which_driver_pool],
                                screen_size_list[0], screen_size_list[1])
    text = input_page.find_element_by_id('com.android.mms:id/embedded_text_editor').text
    assert text == 'Qwerty '
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('检查长按方法')
@pytest.mark.parametrize('case_number', [3])
def test_InputMethod_SCB_func_01_01_01_0003(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    input_page.long_press('switch', device_id_list[which_driver_pool], screen_size_list[0], screen_size_list[1])
    input_page.return_to_launcher(device_id_list[which_driver_pool])


@allure.story('校验主题')
@pytest.mark.parametrize('case_number', [4])
def test_InputMethod_SCB_func_01_01_01_0004(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_theme_setting_page()
    time.sleep(2)
    from page.theme_setting_page import ThemeSettingPage
    theme_setting_page = ThemeSettingPage(get_driver_pool[which_driver_pool])
   # theme_setting_page.back_to_setting_page()
    theme_setting_page.switch_them1()
    #theme_setting_page.switch_them2()
    #theme_setting_page.switch_them3()
    #theme_setting_page.switch_them4()
    # time.sleep(2)
    #截图
    # input_page.screenshot()
    # #比较截图是否一致
    # input_page.compare(r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp4.png',
    #                    r'/Users/xm210407/PycharmProjects/Kika/testcase/TestResult/tmp5.png')

@allure.story('校验字体')
@pytest.mark.parametrize('case_number', [5])
def test_InputMethod_SCB_func_01_01_01_0005(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_font_setting_page()
    time.sleep(2)
    from page.font_setting_page import FontSettingPage
    font_setting_page = FontSettingPage(get_driver_pool[which_driver_pool])
    #font_setting_page.back_to_setting_page()
    font_setting_page.switch_font4()
    #font_setting_page.switch_font2()
    #font_setting_page.switch_font3()
    #font_setting_page.switch_font4()
    time.sleep(2)

@allure.story('校验页面设置')
@pytest.mark.parametrize('case_number', [7])
def test_InputMethod_SCB_func_01_01_01_0007(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_page_setting_page()
    time.sleep(2)
    from page.page_setting_page import PageSettingPage
    page_setting_page = PageSettingPage(get_driver_pool[which_driver_pool])
    #page_setting_page.back_to_setting_page()
    #page_setting_page.check_bubble_capitalization(checkbox='noselect')
    #page_setting_page.check_number_capitalization(checkbox='select')
    page_setting_page.check_slide_capitalization(checkbox='noselect')
    # page_setting_page.to_delay_page()
    # time.sleep(2)
    # from page.key_delay_page import KeyDelayPage
    # key_delay_page = KeyDelayPage(get_driver_pool[which_driver_pool])
    # key_delay_page.check_default_capitalization()
    # key_delay_page.check_determine_capitalization()
    # key_delay_page.adjust_progress_capitalization(size='min')
    #key_delay_page.adjust_progress_capitalization(size='max')
    #key_delay_page.adjust_progress_capitalization(size='middle')
    #key_delay_page.check_determine_capitalization()

    #page_setting_page.check_slide_capitalization()

@allure.story('校验输入设置')
@pytest.mark.parametrize('case_number', [8])
def test_InputMethod_SCB_func_01_01_01_0008(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_input_setting_page()
    time.sleep(2)
    from page.input_setting_page import InputSettingPage
    input_setting_page = InputSettingPage(get_driver_pool[which_driver_pool])
    #input_setting_page.back_to_setting_page()
    #input_setting_page.check_slide_input_capitalization(checkbox='noselect')
    input_setting_page.check_slide_orbit_capitalization(checkbox='select')
    #input_setting_page.check_auto_capitalization(checkbox='select')
    #input_setting_page.check_suggest_capitalization(checkbox='select')
    #input_setting_page.check_automatic_correct_capitalization(checkbox='select')
    #input_setting_page.check_emoji_prediction_capitalization(checkbox='select')
    #input_setting_page.check_double_click_capitalization(checkbox='select')
    #input_setting_page.check_quickly_insert_capitalization(checkbox='select')
    #input_setting_page.check_long_press_capitalization(checkbox='select')
    #input_setting_page.check_experience_plan_capitalization(checkbox='select')

@allure.story('校验音效和振动')
@pytest.mark.parametrize('case_number', [9])
def test_InputMethod_SCB_func_01_01_01_0009(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_voice_setting_page()
    from page.voice_setting_page import VoiceSettingPage
    voice_setting_page = VoiceSettingPage(get_driver_pool[which_driver_pool])
    #voice_setting_page.back_to_setting_page()
    #voice_setting_page.adjust_vib_drag_bar(max)
    #voice_setting_page.adjust_vib_drag_bar(size='max')
    #voice_setting_page.adjust_vib_drag_bar(size='min')
    #voice_setting_page.adjust_vib_drag_bar(size='middle')
    #voice_setting_page.adjust_sound_drag_bar(size='middle')
    #voice_setting_page.adjust_sound_drag_bar(size='max')
    #voice_setting_page.adjust_sound_drag_bar(size='min')
    voice_setting_page.to_sound_effect_page()
    from page.sound_effect_page import SoundEffectPage
    sound_effect_page = SoundEffectPage(get_driver_pool[which_driver_pool])
    #sound_effect_page.back_to_setting_page()
    sound_effect_page.switch_sound1()
    time.sleep(2)
    sound_effect_page.switch_sound2()
    time.sleep(2)
    sound_effect_page.switch_sound3()
    time.sleep(2)
    sound_effect_page.switch_sound4()
    time.sleep(2)
    sound_effect_page.switch_sound5()
    time.sleep(2)
    sound_effect_page.switch_sound6()
    time.sleep(2)
    sound_effect_page.switch_sound7()
    time.sleep(2)
    sound_effect_page.switch_sound8()
    time.sleep(2)
    sound_effect_page.switch_sound9()

@allure.story('校验关于')
@pytest.mark.parametrize('case_number', [10])
def test_InputMethod_SCB_func_01_01_01_0010(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    print('case_number：%s' % case_number)
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_about_setting_page()
    from page.about_setting_page import AboutSettingPage
    about_setting_page = AboutSettingPage(get_driver_pool[which_driver_pool])
    #about_setting_page.back_to_setting_page()
    #about_setting_page.to_disable_service()
    # from page.disable_service_page import DisableServicePage
    # disable_service_page = DisableServicePage(get_driver_pool[which_driver_pool])
    #disable_service_page.check_xpath_cancel()
    #disable_service_page.check_xpath_disable()
    #about_setting_page.check_xpath_privacy_page()
    about_setting_page.check_xpath_user_agreement()

@allure.story('校验语言')
@pytest.mark.parametrize('case_number', [11])
def test_InputMethod_SCB_func_01_01_01_0011(get_device_id_list, get_driver_pool, deliver_event, case_number):
    device_id_list = get_device_id_list
    which_driver_pool = int(deliver_event[case_number])
    input_page = InputPage(get_driver_pool[which_driver_pool])
    screen_size_list.clear()
    get_vm_size(device_id_list[which_driver_pool], screen_size_list)
    print('----- %s -----' % device_id_list)
    os.system(test_adb_data['adb_01_01_01_0001']['textmessage'] % device_id_list[which_driver_pool])
    input_page.find_element_by_id_click('com.android.mms:id/embedded_text_editor')
    time.sleep(2)
    input_page.touch_tap(81, 1468)
    time.sleep(2)
    input_page.touch_tap(170, 2176)
    from page.keyboard_setting_page import KeyboardSettingPage
    keyboard_setting_page = KeyboardSettingPage(get_driver_pool[which_driver_pool])
    keyboard_setting_page.to_language_setting_page()
    from page.language_setting_page import LanguageSettingPage
    language_setting_page = LanguageSettingPage(get_driver_pool[which_driver_pool])
    #language_setting_page.back_to_setting_page()
    #language_setting_page.open_input_menu_search()
    #language_setting_page.close_input_menu_search()
    language_setting_page.add_language_list(language='爪哇文', predict='ast_0_1 ')
    # language_setting_page.del_language_list(language='南非荷兰文')
    # time.sleep(2)
    # language_setting_page.update_layout(layouttext1='AZERTY')




if __name__ == '__main__':
    pytest.main()