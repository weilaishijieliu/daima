from base.base_action import BaseAction
from page.all_contact_page import PageAllContact
from page.contact_info import PageContactInfo
from page.new_add_contact import PageNewAddContact


class Page(BaseAction):

    @property
    def all_contact(self):
        return PageAllContact(self.driver)

    @property
    def contact_info(self):
        return PageContactInfo(self.driver)

    @property
    def new_add_contact(self):
        return PageNewAddContact(self.driver)
