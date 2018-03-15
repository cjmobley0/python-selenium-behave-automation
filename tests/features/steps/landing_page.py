###################################################
#
#


import logging, time

from behave import given, then, use_step_matcher

from tests.resource.pages.home_page import HomePageElements
from tests.resource.properties.main_properties import MainProperties

LOG = logging.getLogger(__name__)

use_step_matcher("re")


@then('validate the following top navigation elements are displayed on the home page')
def validate_the_following_elements_displayed_on_sign_in_page(context):
    test_fail = False
    for row in context.table:
        if hasattr(HomePageElements, row[0]):
            selector = getattr(HomePageElements, row[0])

            if context.driver.find_element_by(selector) is not None:
                print("\tPASSED - " + str(row[0]))
            else:
                test_fail = True
                print("\tFAILED - " + str(row[0]))

        else:
            LOG.info(" '" + str(row) + "' is not a valid selector in SignInPageObjects")
            raise Exception(LOG)

    if test_fail:
        raise AssertionError("One of the elements have failed to load")