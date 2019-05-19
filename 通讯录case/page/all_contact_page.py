from selenium.webdriver.common.by import By

from base.base_action import BaseAction

add_contact = By.ID, "com.android.contacts:id/floating_action_button"
class PageAllContact(BaseAction):

    def click_add_contact(self):
        self.click(add_contact)