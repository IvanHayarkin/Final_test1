import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml', encoding='utf-8') as f:
        locators = yaml.safe_load(f)
        for locator in locators['xpath'].keys():
            ids[locator] = (By.XPATH, locators['xpath'][locator])
        for locator in locators['css'].keys():
            ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f'Send {word} to {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while handling {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception while clicking {element_name}')
            return False
        logging.info(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while getting text from {element_name}')
            return None
        logging.info(f'Field {element_name} contains text: {text}')
        return text

# Enter text methods
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password')

    # def add_title(self, word):
    #     self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_POST'], word, description='post title')
    #
    # def add_description(self, word):
    #     self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION_POST'], word, description='post description')
    #
    # def add_content(self, word):
    #     self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_POST'], word, description='post content')
    #
    # def add_name(self, word):
    #     self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_YOUR_NAME'], word, description='contact name')
    #
    # def add_email(self, word):
    #     self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_YOUR_EMAIL'], word, description='contact email')
    #
    # def add_contact_content(self, word):
    #     self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word, description='contact content')

# Click button methods
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_about_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_ABOUT_BTN'], description='about option')

    # def click_add_post_button(self):
    #     self.click_button(TestSearchLocators.ids['LOCATOR_ADD_POST'], description='add post')
    #
    # def click_save_post_button(self):
    #     self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_POST'], description='save post')
    #
    # def click_contact_button(self):
    #     self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT'], description='click contact')
    #
    # def click_contact_us_button(self):
    #     self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='click contact us')

# Get text methods
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error text')

    def login_success(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SUCCESS'], description='login success')

    def about_click_success(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ABOUT_PAGE'], description='about success')

    # def find_new_post_title(self):
    #     return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_FIND_NEW_POST'], description='new post title')

# Get properties
    def check_title_size(self):
        return self.get_element_property(TestSearchLocators.ids['LOCATOR_ABOUT_PAGE'], 'font-size')


# Single method
#     def get_alert_message(self):
#         time.sleep(1)
#         logging.info("Get alert message")
#         txt = self.get_alert_txt()
#         logging.info(f"Alert message is {txt}")
#         return txt
