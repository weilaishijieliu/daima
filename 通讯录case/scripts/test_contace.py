from base.analyze_data import analyze_data
from base.get_driver import get_driver
from page.page import Page
import pytest
class TestContact:

    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_data("contact_data.yaml", "test_contact_tel"))
    def test_contact_tel(self, args):
        name = args['name']
        phone = args['phone']
        self.page.all_contact.click_add_contact()
        self.page.new_add_contact.input_username(name)
        self.page.new_add_contact.input_tel(phone)
        self.page.new_add_contact.save_contact()
        assert self.page.contact_info.get_contact_name_text() == name

    @pytest.mark.parametrize('args', analyze_data("contact_data.yaml", "test_contact_email"))
    def test_contact_email(self, args):
        name = args['name']
        email = args['email']
        self.page.all_contact.click_add_contact()
        self.page.new_add_contact.input_username(name)
        self.page.new_add_contact.input_email(email)
        self.page.new_add_contact.save_contact()
        assert self.page.contact_info.get_contact_name_text() == name