from public.base_function import BaseFunction

"""
    词库设置页面
"""


class ThesaurusSettingPage(BaseFunction):
    # 进入通讯录词库页面
    def to_address_book_thesaurus(self):
        self.find_element_by_text_click('通讯录词库')
        from page.address_book_thesaurus import AddressBookThesaurusPage
        return AddressBookThesaurusPage(self.driver)
