import os, time, logging
from behave import given, when, then
from behave import use_step_matcher
from tests.config import config
from tests.resource.driver.webdriverAPI import WebDriverApi

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

    if endpoint in config:
        context.driver.browser_launch(config[endpoint]['url'])
    else:
        LOG.info(" '" + endpoint + "' is not a configured endpoint.")
        LOG.info("Check that endpoint exists in config.yml")
        raise Exception()


@then('validate the "(?P<element>.*)" is displayed on the sign in page')
def validate_the_element_is_displayed(context, element):
    context.driver.find_element_by("xpath", config['page_elements']['sign_in_page'][element])


@given('sleep for "(?P<time_in_sec>.*)" seconds')
def sleep_for_seconds(context, time_in_sec):
    time.sleep(time_in_sec)
