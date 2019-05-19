from selenium.webdriver.common.by import By

from base.base_action import BaseAction

name = By.XPATH, "//*[@text='姓名']"
nickname = By.XPATH, "//*[@text='昵称']"
tel = By.XPATH, "//*[@text='电话']"
email = By.XPATH, "//*[@text='电子邮件']"

class PageNewAddContact(BaseAction):

    def input_username(self, value):
        self.input(name, value)

    def input_nickname(self,value):
        self.input(nickname, value)

    def input_tel(self, value):
        self.input(tel, value)

    def input_email(self, value):
        self.input(email, value)

    def save_contact(self):
        self.click_back()