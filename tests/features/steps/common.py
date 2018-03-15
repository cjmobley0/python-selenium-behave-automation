import logging, time
import ast  #Translate unitcode -> python object

from behave import given, then
from behave import use_step_matcher

from tests.resource.driver.webdriverAPI import WebDriverApi
from tests.resource.services.auto_service import AutomationServices
from tests.resource.properties.main_properties import MainProperties

# GLOBAL DICT
web_dict = {}
LOG = logging.getLogger(__name__)
use_step_matcher("re")

#Class instanciations
autoServices = AutomationServices()

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
        LOG.info("Check that endpoint exists in properties file")
        raise Exception(LOG)


@then('validate the "(?P<element>.*)" is displayed on the "(?P<page_type>.*)" page')
def validate_the_element_is_displayed(context, element, page_type):

    # Dynamic class setter
    elem_page_type = autoServices.getPageType(page_type)

    if hasattr(elem_page_type, element):
        selector = getattr(elem_page_type, element)
        web_element = context.driver.find_element_by(selector)
    else:
        LOG.info(" '" + element + "' is not a valid selector in " + page_type)
        raise Exception(LOG)


@when('the user clicks the "(?P<element>.*)" (?:button|element) on the "(?P<page_type>.*)" page')
def the_user_clicks_the_element(context, element, page_type):

    # Dynamic class setter: Gets page type associated with element
    elem_page_type = autoServices.getPageType(page_type)

    if hasattr(elem_page_type, element):
        selector = getattr(elem_page_type, element)
        context.driver.find_element_by(selector).click()
    else:
        LOG.info(" '" + element + "' is not a valid selector in " + page_type)
        raise Exception(LOG)

@then('validate the user is navigated to the "(?P<url>.*)" page')
def validate_user_is_navigated_to_the_page(context, url):
    curr_url = context.driver.instance.current_url

    if getattr(MainProperties, url) == curr_url:
        pass
    else:
        LOG.info(" 'Current URL: " + curr_url + " does not match the expected URL: " + str(getattr(MainProperties, url))  + "' ")

@given('sleep for "(?P<time_in_sec>.*)" seconds')
def sleep_for_seconds(context, time_in_sec):
    time.sleep(time_in_sec)
