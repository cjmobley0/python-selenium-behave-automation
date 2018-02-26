import logging
import time

from behave import given, then
from behave import use_step_matcher

from tests.resource.driver.webdriverAPI import WebDriverApi
from tests.resource.pages.page_elements import SignInPageObjects
from tests.resource.properties.main_properties import MainProperties

# GLOBAL DICT
web_dict = {}

LOG = logging.getLogger(__name__)

use_step_matcher("re")


@given('START (?P<browser>.*) browser')
def start_browser(context, browser):
    context.driver = WebDriverApi()
    context.driver.instance(browser)


@given('END')
def end_webdriver(context):
    context.driver.tearDown()


@given('navigate to "(?P<endpoint>.*)" page')
def navigate_to_page(context, endpoint):

    if hasattr(MainProperties, endpoint):
        context.driver.browser_launch(MainProperties.hr_prod_url)
    else:
        LOG.info(" '" + endpoint + "' is not a configured endpoint.")
        LOG.info("Check that endpoint exists in /properties/main_properties.py")
        raise Exception()


@then('validate the "(?P<element>.*)" is displayed on the sign in page')
def validate_the_element_is_displayed(context, element):
    context.driver.find_element_by(SignInPageObjects.HACKERRANK_LOGO)


@given('sleep for "(?P<time_in_sec>.*)" seconds')
def sleep_for_seconds(context, time_in_sec):
    time.sleep(time_in_sec)
