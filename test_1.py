import yaml
from pagetest import OperationsHelper
import logging
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_error_text(browser):
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_error_text() == '401'


def test_login_positive(browser):
    logging.info('Test login_positive Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.login_success() == f'Hello, {testdata["login"]}', 'test_login_positive FAILED'


def test_contact_us(browser):
    logging.info('Test add_post Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.add_name(testdata['u_name'])
    testpage.add_email(testdata['u_email'])
    testpage.add_contact_content(testdata['content_field'])
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == 'Form successfully submitted', 'test contact us FAILED!'


