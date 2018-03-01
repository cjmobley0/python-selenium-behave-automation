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
        selector = getattr(MainProperties, endpoint)
        context.driver.browser_launch(selector)
    else:
        LOG.info(" '" + endpoint + "' is not a configured endpoint.")
        LOG.info("Check that endpoint exists in /properties/main_properties.py")
        raise Exception(LOG)


@then('validate the "(?P<element>.*)" is displayed on the sign in page')
def validate_the_element_is_displayed(context, element):
    if hasattr(SignInPageObjects, element):
        selector = getattr(SignInPageObjects, element)
        web_element = context.driver.find_element_by(selector)
        print (web_element)
    else:
        LOG.info(" '" + element + "' is not a valid selector in SignInPageObjects")
        raise Exception(LOG)

@then('validate the following top navigation elements are displayed on the home page')
def validate_the_following_elements_displayed_on_sign_in_page(context):
    test_fail = False
    for row in context.table:
        if hasattr(SignInPageObjects, row[0]):
            selector = getattr(SignInPageObjects, row[0])

            if context.driver.find_element_by(selector) != None:
                print("\tPASSED - " + str(row[0]))
            else:
                test_fail = True
                print("\tFAILED - " + str(row[0]))

        else:
            LOG.info(" '" + str(row) + "' is not a valid selector in SignInPageObjects")
            raise Exception(LOG)

    if test_fail:
        raise AssertionError("One of the elements have failed to load")




@given('sleep for "(?P<time_in_sec>.*)" seconds')
def sleep_for_seconds(context, time_in_sec):
    time.sleep(time_in_sec)
