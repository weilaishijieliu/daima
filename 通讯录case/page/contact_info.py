from selenium.webdriver.common.by import By

from base.base_action import BaseAction

contact_name = By.ID, "com.android.contacts:id/large_title"
class PageContactInfo(BaseAction):

    def get_contact_name_text(self):
        return self.get_text(contact_name)